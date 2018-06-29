'''
Fits a function to the spectra
'''

import numpy as np
import numpy.polynomial.polynomial as npp
import scipy.optimize as spop

from mathutils import gaussian, lorentzian
import cnvrgtests as ct

def yupdate(x,y,p,sigmabin=100.0,func=gaussian):
    '''
    Takes in x and y data, and a fitted polynomial and returns an
    array of the y values with the g(x) values subtracted from it. 
    G(x) is the function fit to the x values.
    '''
    #Getting coordinates of x and y of the bottom of the line
    mindex = y.argmin()
    x_of_ymin, ymin = x[mindex], y[mindex]
    xmin, xmax = x[0], x[-1]
    #Initial guesses for curve_fit to get the optimized parameters
    params = np.array([ymin - p(x_of_ymin),x_of_ymin, x.ptp()/sigmabin])
    #curve_fit getting the optimal parameters
    res = y-p(x)
    params, pcov = spop.curve_fit(func, x, res, params)
    A, mu, sigma = params
    #Getting an array of g(x) values
    g = func(x,A, mu, sigma)
    ynew = y - g
    return ynew, res, params


def polycntm(x,y,deg,rtol=1e-3,fullout=False,maxiter=50):
    '''
    Fits a polynomial continuum of degree deg to the data 
    '''
    #Initializing Variables
    p = npp.Polynomial([0]*(deg+1))
    keepgoing = True
    counter = 0
    datalist, linelist, reslist, gpmslist = [y],[],[],[]
    #Iterations
    while keepgoing and counter < maxiter:
        pold, p = p, npp.Polynomial.fit(x,y,deg)
        test_result, test_bool = ct.midpnttest(pold.coef,p.coef,rtol)
        if np.all(test_bool):
            break
        linelist.append(p)
        y, res, params = yupdate(x,y,p)
        datalist.append(y)
        reslist.append(res) 
        gpmslist.append(params)
        counter += 1

    #legacy code used to create plots of each iteration of yupdate
    #if counter >= maxiter:
    #   print("Exceeded maximum amount of itinerations") 
    #    print(test_result)
    #if fullout:
    #    datalist.__delitem__(len(datalist)-1)
    #    return p, datalist, linelist, reslist, gpmslist
    return p

def specfit(x,y,deg=1,rtol=1e-3,fullout=False,maxiter=50,funct=gaussian):
    '''
    Runs polycntm on given data to find the polynomial continuum of the
    degree given, makes array of x values inputted to polycntm's
    outputted polynomial and then subtracts those values from the
    original y values. Returns the parameters of a function fit to the
    data.
    '''
    #used along with viewintermediates.py to create plots of yupdate
    #cntm, d, l, r, g = polycntm(x,y,deg,rtol,fullout,maxiter)

    cntm = polycntm(x,y,deg,rtol,fullout,maxiter)

    ynew, res, gparams = yupdate(x,y,cntm,func=funct)
   
    return cntm, gparams

