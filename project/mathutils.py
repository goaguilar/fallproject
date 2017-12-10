'''Useful Math functions'''
import numpy as np

#Defines a gaussian function 
def gaussian(x,A,mu,sigma):
    '''
    Returns a guassian based on the x values given A,mu, and sigma
    '''
    return A*np.exp(-0.5*((x - mu)/sigma)**2.0)

#Defines a Lorentzian function
def lorentzian(x,A,mu,sigma):
    '''
    Returns a lorentzian function based on the x values, where p is an
    array containing the parameters.
    '''
    return A*(sigma**2)/((x - mu)**2 + sigma**2)
