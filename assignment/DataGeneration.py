#!/usr/bin/env python
# coding: utf-8
import numpy as np

def generate_data(N, global_sigma=1, d=5):
    '''
    Function to generate normally distributed point clouds based around the corners and the base of a cube
    
    Parameters
    ----------
    N: int
    Number of observations to generate
    global_sigma: float, optional
    Value for the standard deviation of all independent normal distributions used for the creation of the point clouds
    d: int or float, optional
    $2xd = edge length of the cube
    
    Returns
    -------
    out: ndarray of shape (N,9,3)
    Contains N observations of nine points described by three spacial coordinates
    '''
    # The point here is to consider 9*3 values as a single array of 27 elements.
    # First 3 =mux1,muy1,muz1, the 2nd 3=mux2,muy2,muz2, etc...
    mu1 = [0, 0, 0]
    mu2 = [d, d, d]
    mu3 = [-d, d, d]
    mu4 = [d, -d, d]
    mu5 = [d, d, -d]
    mu6 = [-d, -d, d]
    mu7 = [-d, d, -d]
    mu8 = [d, -d, -d]
    mu9 = [-d, -d, -d]
    mean_nd = mu1 + mu2 + mu3 + mu4 + mu5 + mu6 + mu7 + mu8 + mu9
    cov_nd = np.zeros((27,27))
    np.fill_diagonal(cov_nd, global_sigma)
    
    # Call the multivariate normal PDF
    data = np.random.multivariate_normal(mean=mean_nd, cov=cov_nd, size=N)

    # Reshape, i.e. group 27 numbers into 9 x 3D vectors
    return data.reshape(N, 9, 3)