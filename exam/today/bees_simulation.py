import numpy as np
import pandas as pd

dim=2

# Null vector
def NullVector():
    return np.zeros(shape=(dim))

# Function to compute the interaction force between bees
def MutualForce(r1, r2, Strength=0.01):
    '''
    vec{F}_{on 1 from 2} = a * \vec{r21}/r21
    '''
    r21 = r2 - r1
    d21 = np.linalg.norm(r21)
    if d21 == 0:
        return np.zeros(dim)  # To avoid division by zero
    return Strength * r21 / d21

# Add some randomness in bees motion
def RandomdR(Strength=0.01):
    '''
    Random position shift of strengh a
    '''
    return Strength * np.random.randn(dim)


# Perform reflexion
def WallReflecion(r, v, L):
    rx, ry = r[0], r[1]
    vx, vy = v[0], v[1]
    if   rx>L and ry<L: return np.array([-vx,  vy])
    elif rx>L and ry>L: return np.array([-vx, -vy])
    elif rx<L and ry>L: return np.array([ vx, -vy])
    elif rx<0 and ry>0: return np.array([-vx,  vy])
    elif rx<0 and ry<0: return np.array([-vx, -vy])
    elif rx>0 and ry<0: return np.array([ vx, -vy])
    else              : return v
    
    
# Flower field attraction lattice (static field all over the space)
def FlowerLatticeForce(r, a=10, L=100, Length=30, Strength=0.01):
    '''
    Choose spacing between flowers in the lattice of 
    spatial period a=10m, over a squared field of side L=100m
    '''
    
    # Precision for future calculations
    eps = 1e-8
    
    # Create the lattice using
    x1d = np.array([i*a for i in range(int(L/a)+1)])
    if dim==2:
        x, y = np.meshgrid(x1d, x1d)
        nodes = np.array([x, y])
        v = np.array( [r[0]-x, r[1]-y] )
        d = np.sqrt( np.sum(v**2, axis=0) )
        d = d[np.newaxis, :, :]+eps
        return np.sum( - Strength * np.exp(-d/Length) * v/d, axis=(1, 2)) 
    elif dim==3:
        x, y, z = np.meshgrid(x1d, x1d, x1d)
        nodes = np.array([x, y, z])
        v = np.array( [r[0]-x, r[1]-y, r[2]-z] )
        d = np.sqrt( np.sum(v**2, axis=0) )
        d = d[np.newaxis, :, :, :]+eps
        return np.sum( - Strengh * np.exp(-d/Length) * v/d, axis=(1, 2, 3)) 
    else:
        raise NameError(f'd={dim}, while it must be 2 or 3')
        
        
        
        
def run_bees_simulation(steps=50000, dt=0.05     ,
                       attraction=1, field=1     ,
                       g_attra=0.1 , g_field=2.8 ,
                       box=1       , lbox=300    , 
                       noise=0     , g_noise=0.01,
                       run=0):
    
    '''
    This function run the simulation of two bees for a given setup,
    defined as below, and save the data as a dataframe (time, positions 
    and velocities of each bees in 2 dimensions).
    
    Parameters
    -----------
      step       = number of simulations
      dt         = time duration between 2 steps (in ms)
      attraction = 0/1 enable attraction between two bees
      field      = 0/1 enable the presence of flower field (formed as a lattice)
      g_attra    = float (default 0.1) is the strength of the attraction force
      g_field    = float (default 2.8) is the strength of the flower field force
      box        = 0/1 enable a square box to which bees will 'reflect' over its walls
      lbox       = number being the size of the box
      noise      = 0/1 enable some heratic component in bees motion
      g_noise    = stength of random noise
      run        = number of the run
    
    Returns
    -------
      The name of the saved csv file (str)
      
    '''
    
    
    # Simulation parameters
    # ----------------------
    STEPS      = steps      # Number of time steps in the simulation
    DT         = dt         # Time step (in ms)
    ATTRACTION = attraction # Enable attraction force between the bees
    FIELD      = field      # Add a field of flower with attraction
    BOX        = box        # Add a box creating bound of a bee
    LBOX       = lbox       # Size of the box containing the bees
    NOISE      = noise      # Adding a random force
    RUN        = run        # Run number to keep track of several

    # Initialize positions and velocities of the two bees
    bee1_pos = np.zeros(shape=(dim)) + 50.5  
    bee2_pos = np.zeros(shape=(dim)) + 75.0
    bee1_vel = np.zeros(shape=(dim))
    bee2_vel = np.zeros(shape=(dim))
    bee1_vel = np.array([+1.0, +1.0])
    bee2_vel = np.array([+0.2, +1.0])

    # Lists to store the positions of the bees over time
    bee1_positions = [bee1_pos.copy()]
    bee2_positions = [bee2_pos.copy()]
    bee1_velocitys = [bee1_vel.copy()]
    bee2_velocitys = [bee2_vel.copy()]

    # Simulation loop
    for s in range(STEPS):

        # Compute interaction forces
        if ATTRACTION:
            Fi1 = MutualForce(bee1_pos, bee2_pos, Strength=g_attra)
            Fi2 = MutualForce(bee2_pos, bee1_pos, Strength=g_attra)
        else:
            Fi1, Fi2 = NullVector(), NullVector()        

        # Compute the attraction from flowers
        if FIELD:
            Ff1 = FlowerLatticeForce(bee1_pos, a=10, L=LBOX, Length=0.1, Strength=g_field)
            Ff2 = FlowerLatticeForce(bee2_pos, a=10, L=LBOX, Length=0.1, Strength=g_field)
        else:
            Ff1, Ff2 = NullVector(), NullVector()

        # Random force
        if NOISE:
            dR1noise = RandomdR(Strength=g_noise)
            dR2noise = RandomdR(Strength=g_noise)
        else:
            dR1noise, dR2noise = NullVector(), NullVector()

        # Perform reflexion on the box
        if BOX:
            bee1_vel = WallReflecion(bee1_pos, bee1_vel, L=LBOX)
            bee2_vel = WallReflecion(bee2_pos, bee2_vel, L=LBOX)

        # Update velocities based on forces and noise
        bee1_vel += (Fi1 + Ff1) * DT
        bee2_vel += (Fi2 + Ff2) * DT

        # Update positions based on updated velocity
        bee1_pos += bee1_vel * DT + dR1noise 
        bee2_pos += bee2_vel * DT + dR2noise 

        # Store positions and velocities
        bee1_positions.append(bee1_pos.copy())
        bee2_positions.append(bee2_pos.copy())
        bee1_velocitys.append(bee1_vel.copy())
        bee2_velocitys.append(bee2_vel.copy())

    # Convert positions to arrays for easy plotting
    bee1_positions = np.array(bee1_positions)
    bee2_positions = np.array(bee2_positions)
    bee1_velocitys = np.array(bee1_velocitys)
    bee2_velocitys = np.array(bee2_velocitys)
    
    # Save dat in a csv file
    df = pd.DataFrame({
     'tms': np.arange(STEPS+1)*DT, 
     'Rx1': bee1_positions[:,0],
     'Ry1': bee1_positions[:,1],
     'Rx2': bee2_positions[:,0],
     'Ry2': bee2_positions[:,1],
     'Vx1': bee1_velocitys[:,0],
     'Vy1': bee1_velocitys[:,1],
     'Vx2': bee2_velocitys[:,0],
     'Vy2': bee2_velocitys[:,1],
    })

    # Name creation
    csv_name  = f'beesMotion_BOX-{BOX}_LBOX-{LBOX}'
    csv_name += f'_ATTRACTION-{ATTRACTION}_gATTRA-{g_attra:.2f}'
    csv_name += f'_FIELD-{FIELD}_gFIELD-{g_field:.2f}'
    csv_name += f'_NOISE-{NOISE}_RUN-{RUN}.csv'
    
    # Save the CSV file and return its name
    df.to_csv(csv_name, index=False)
    return csv_name
