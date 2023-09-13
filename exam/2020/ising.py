import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class spinLattice:
    
    def __init__(self, N):
        self.spins = 2*np.random.randint(2, size=(N,N))-1
        

    def align(self):
        '''
        Align all spins together
        '''
        self.spins = np.zeros_like(self.spins) + 1

        
    def antialign(self):
        '''
        Anti-align all spins. Possible if N is even (raise an error otherwise).
        '''
        N = self.spins.shape[0]
        if N%2 != 0:
            raise NameError('Anti-alligned spin system must have an even N')
        l1 = np.zeros(N) + 1
        l1[::2] = -1
        l2 = np.zeros(N) + 1
        l2[1::2] = -1
        self.spins = np.array([l1, l2]*int(N/2))
        

    def randomize(self):
        '''
        Randomely flip spins.
        '''
        flip = 2*np.random.randint(2, size=self.spins.shape)-1
        self.spins *= flip

        
    def perturbate(self, x0, y0, R):
        '''
        Put all spins in -1 state in a give region
        defined as a circle centered in (x0, y0) and
        of radius R. x0, y0 and R are expressed in lattice
        unit.
        '''
        N = self.spins.shape[0]
        x, y = np.meshgrid(np.arange(N), np.arange(N))
        x, y = x.flatten(), y.flatten()

        d = np.sqrt((x-x0)**2  + (y-y0)**2)
        xPert, yPert = x[d<R], y[d<R]
        self.spins[xPert, yPert] = -1

        
    def plot(self):
        '''
        Plotting a snapshot of the 2D spins lattice.
        '''
        plt.gca().xaxis.set_visible(False)
        plt.gca().yaxis.set_visible(False)
        plt.imshow(self.spins.copy(), cmap='BuPu', origin='lower', vmax=+1, vmin=-1)


    def energy(self):
        '''
        Compute and return the energy of the lattice, 
        normalized to the number of spins.
        '''
    
        # Prepare shifted arrays for vectorized computation
        sPad = np.pad(self.spins, (1, 1)) # Padding with 0
        sUp = sPad[0:-2, 1:-1]            # Bring up neighbour to the current node
        sDo = sPad[2:  , 1:-1]            # Bring down neighbour to the current node
        sLe = sPad[1:-1, 0:-2]            # Bring left neighbour to the current node
        sRi = sPad[1:-1, 2:  ]            # Bring right neighbour to the current node
        
        # energy = -1/4 s*up + s*down + s*left + s*right
        energy = -1./4. * self.spins * (sUp+sDo+sLe+sRi)
        
        # Sum over the lattice
        return energy.sum() / self.spins.size

    
    def magnetization(self):
        '''
        Compute and return the magnetization of the spin lattice,
        normalized to the number of spins.
        '''
        return self.spins.sum() / self.spins.size


    def entropy(self):
        '''
        Compute and return the entropy of the system. For a spin-1/2 system, the
        number of configuration for a given microstate is N! / (N[up]! N[down]!).
        Due to numerical consideration, the Stirling’s approximation is used:
           ln(x!) ~ x ln(x) - x
        '''
        Nup = np.count_nonzero(self.spins== 1)
        Ndo = np.count_nonzero(self.spins==-1)    
        if Nup != 0 and Ndo !=0 :
            return (Nup+Ndo) * np.log(Nup+Ndo) - Nup * np.log(Nup) - Ndo * np.log(Ndo)
        else:
            return 0


    def thermalEvolution(self, T, n=-1):
        '''
        Update the spin lattice based on a Metropolis algorithm.
        The cost of flipping every spins is computed in a vectorized manner.
        A flipping decision is computed for each spin, based on energy gain
        or thermal fluctuations. Finally, n random nodes are selected 
        and they are then flipped or not, based on the precedently computed
        decision. By default, n is set to 10% of the spins.
        
        Modify in place the spin lattice, and return a copy of the modified 
        spin lattice.
        '''
        
        # Prepare shifted arrays for vectorized computation
        sPad = np.pad(self.spins, (1, 1))     # Padding with 0
        sUp = sPad[0:-2, 1:-1]                # Bring up neighbour to the current node
        sDo = sPad[2:  , 1:-1]                # Bring down neighbour to the current node
        sLe = sPad[1:-1, 0:-2]                # Bring left neighbour to the current node
        sRi = sPad[1:-1, 2:  ]                # Bring right neighbour to the current node
        
        # Get the number of random sites to modify (50% of the lattice by default)
        if n == -1:
            n = int(self.spins.size * 0.5)
        elif n > self.spins.size:
            raise NameError('Number of sites to be changed must low than spins sites')
        
        # Choose random sites
        pts = np.random.randint(low=0, high=self.spins.shape[0], size=(n, 2))
        Xs, Ys = pts[:, 0], pts[:, 1]
    
        # Energy cost
        cost = 2.0 * self.spins * (sUp+sDo+sLe+sRi)
    
        # Conditions to flip the spin
        flip  = (cost < 0) | (np.random.rand(*self.spins.shape) < np.exp(-cost/T))
    
        # Update the configuration of these sites
        self.spins[Xs, Ys] *= -1 * flip[Xs, Ys] + 1 * ~flip[Xs, Ys]

        # Return the spin lattice
        return self.spins.copy()
        
        
    def twoPtsCorr(self, T, nEvolution):
        '''
        Compute the correlation function as function of the distance:
            G(r) = < si-<si> > * <sj - <sj> >
        where r is the distance d(i, j) between spin i and spin j.
        The mean are computed over Ntime thermal evolutions. In practice,
        the spin in the middle of the lattice is taken as reference. What
        is computed is then:
           G(r) = < s0-<s0> > * <sj - <sj> >
            
        First a serie of nEvolution spin states are generated at temperature T
        leading to a (Ntime, N, N) array where the first dimension
        is the temporal evolution at thermal equilibrium.
            
        The state of the spin Lattice is not affected by the calculation.

        Return 2 1D-array of shape (N*N - 1) correponding to all pairs (0, j)
          - r (array of distance), g (array of correlations)
        '''

        # Save initial state
        initState = self.spins.copy()
        
        # Computing nEvolution states of the spin lattice
        a = np.array([self.thermalEvolution(T) for _ in np.arange(nEvolution)])

        # Setup the spin state as it was
        self.spins = initState
        
        # Take the center of the lattice
        N = self.spins.shape[1]
        x0, y0 = int(N/2), int(N/2)
        s0 = a[:, x0, y0]
        
        # Take all the other spins, excluding (x0, y0)-node.
        xj, yj = np.meshgrid(np.arange(N), np.arange(N))
        xj, yj = xj.flatten(), yj.flatten()
        noCenter = (xj!=x0) | (yj!=y0)
        xj, yj = xj[noCenter], yj[noCenter] 
        sj = a[:, xj, yj]
        
        # Compute the distances
        r = np.sqrt((xj-x0)**2 + (yj-y0)**2)
        
        # Compute mean-substracted (reduced) spins
        s0r = s0 - s0.mean()
        sjr = sj - np.mean(sj, axis=0)
        
        # Compute G(r)
        g = np.mean(sjr * s0r[:, np.newaxis], axis=0)
        
        # Sort points by increasing radius
        sort = np.argsort(r)

        # Return the radius and 2-points correlations.
        return r[sort], g[sort]


    def simulatePhaseTransition(self, Tmin=0.1, Tmax=5, nT=50, 
                                Nther=150, Nmeas=10, Nswitch=-1,
                                reset=False, random=False, revert=False):
    
        '''
        Run a metropolis simulation on tje spin lattice using
        Nther iterations for thermalization of the system and Nmeas 
        iterations to measure system properties. Those are done for each
        temperatures, scanning from Tmin to Tmax using nT steps.
    
        The state of the spin lattice is not modified by a simulation.

        Returning several 1D np.array as function of temperature:
          - temperature, energy, magnetization, entropy
        
        Options:
          - Nther   [default:   150]: number of thermal evolutions before measuring
          - Nmeas   [default:    10]: number of thermal evolution to average observables
          - Nswitch [default:   10%]: number of spins which are possibly flipped in one thermal evolution
          - reset   [default: false]: reset spin state for each temperature
          - random  [default: false]: random initial state, otherwise the
                                      lowest energy configuration is taken
          - revert [default: false]: scan temperatures from hottest to coldest.
        '''

        # Save initial state
        initState = self.spins.copy()
        
        # Initialize arrays
        Ts = np.linspace(Tmin, Tmax, nT)
        Es = np.zeros(nT)
        Ms = np.zeros(nT)
        Ss = np.zeros(nT)
        
        if revert:
            Ts = Ts[::-1]
            
        # Helper function to initialize the spin lattice
        def initState(rand):
            if rand:
                self.randomize()
            else:
                self.align()
    
        # Initial state as aligned spins - to avoid domains.
        initState(random)    

        # Loop over temperatures
        for iT, T in enumerate(Ts):
        
            # Container for this temperature
            e, m, s = np.zeros(Nmeas), np.zeros(Nmeas), np.zeros(Nmeas)
        
            # Reset state if the option is enabled
            if reset:
                initState(random)   
        
            # Thermalization
            for iTh in range(Nther):
                self.thermalEvolution(T, n=Nswitch)

            # Compute energies and magnetism
            for iM in range(Nmeas):
                self.thermalEvolution(T, n=Nswitch)
                e[iM] = self.energy()
                m[iM] = self.magnetization()
                s[iM] = self.entropy()

            # Avergage all measurements for this temperaturs
            Es[iT] = np.mean(e)
            Ms[iT] = np.mean(m)
            Ss[iT] = np.mean(s)

        # Setup the spin state as it was
        self.spins = initState

        # Return the results
        return Ts, Es, Ms, Ss


    def animate(self, T, nEvolutions=50, saveName='', interval=50):

        '''
        Create a animation of spin lattice evolution at a temperature
        T, for nEvolutions steps. The output video can be saved under
        'saveName' (if empty, the video is not saved).

        The state of the spin lattice is not modified by an animation.

        Return the animation. To be displayed in a notebook, do
        >>> from IPython.display import HTML
        >>> anim = s.animate(T, N)
        >>> HTML(anim.to_html5_video())
        '''

        initState = self.spins.copy()
        imgs = [self.thermalEvolution(T) for _ in range(nEvolutions)]
        self.spins = initState
        
        def init():
            img.set_data(imgs[0])
            return (img,)

        def animate(i):
            img.set_data(imgs[i])
            return (img,)

        fig = plt.figure()
        ax  = fig.gca()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        img = ax.imshow(imgs[0],  cmap='BuPu', origin='lower')
        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(imgs),
                                       interval=interval, blit=True, save_count=len(imgs))
        plt.tight_layout()
        
        # Set up formatting for the movie files
        if saveName:
            anim.save('{}.gif'.format(saveName), writer='imagemagick', fps=60)

        return anim
