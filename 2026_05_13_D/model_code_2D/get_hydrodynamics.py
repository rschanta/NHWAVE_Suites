import numpy as np
from scipy.optimize import brentq
def get_hydrodynamics(var_dict):
    ## UNPACK -----------------------------------------------------------------
    T = var_dict['PER']
    d = var_dict['DEP']
    ## [END] UNPACK -----------------------------------------------------------
    

    # Define gravity and fluid density
    g = 9.81
    
    # Define orbital period
    omega = 2 * np.pi / T
    
    # Linear dispersion relation used for root finding
    def disp_relation(k):
        return omega**2 - g * k * np.tanh(k * d)
    
    # Use Brent's Method to solve for wave number k, define wavelength
    k = brentq(disp_relation, 1e-12, 10)
    L = 2 * np.pi / k
    
    # Calculate celerity and group velocity
    c = omega/k
    n = 0.5*(1+(2*k*d)/np.sinh(2*k*d))
    cg = n*c
    
    return {'k': k,'L': L,
            'n': n, 'c': c, 'cg': cg}