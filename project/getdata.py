import numpy as np

def getdata (filenametxt):
    '''
    Reads a txt file and generates containers for the x and y data
    '''
    d = np.genfromtxt(filenametxt)
    xdata,ydata = d[:,0], d[:,1]
    return xdata,ydata
