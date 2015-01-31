import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import pi
import scipy.integrate as sci
from scipy.integrate import quad
from scipy.special import erf
import argparse

# Physics 20 Assignment 3


# Problem 1, mass on a string, using Euler method

def spring(xi, vi, h):
    '''
    This function implements the explicit Euler method to numerically work with
    the motion of a mass on a string. Plots of x and v vs time are made for a
    few cycles of oscillation. This function takes initial conditions, xi and
    vi, and the step size is h.
    '''
    xlist = []
    vlist = []
    tlist = np.arange(0, 10, h)
    for t in tlist:
        xlist.append(xi)
        vlist.append(vi)
        xi, vi = xi + h * vi, vi - h * xi
    plt.figure()
    plt.plot(tlist, xlist, label = "x plot")
    plt.plot(tlist, vlist, label = "v plot")
    plt.legend()
    plt.savefig('spring.pdf')



# Problem 2, comparison between analytic and numerical solutions errors

def analytic(xi, vi, h):
    '''
    This function compares the analytic and numerical solutions to the mass on
    a spring, and plots the errors for comparioson. This deals with the explicit
    Eulers method.
    '''
    x_analytic = []
    v_analytic = []
    xlist = []
    vlist = []
    tlist = np.arange(0, 10, h)

    x_analytic = xi * np.cos(tlist) + vi * np.sin(tlist)
    v_analytic = - xi * np.sin(tlist) + vi * np.cos(tlist)

    for t in tlist:
        xlist.append(xi)
        vlist.append(vi)
        xi, vi = xi + h * vi, vi - h * xi
    plt.figure()
    plt.plot(tlist, xlist, 'b-', label = "x plot")
    plt.plot(tlist, vlist, 'g-', label = "v plot")
    plt.plot(tlist, x_analytic, 'b--', label = "x analytic")
    plt.plot(tlist, v_analytic, 'g--', label = "v analytic")
    plt.legend()
    plt.savefig('analytic.pdf')


# Problem 3, truncation error

def truncation(xi, vi, h):
    '''
    This function plots max value for the difference between x analytic and
    numeric vs h to show the truncation error.
    '''
    x_analytic = []
    hlist = h * np.logspace(-2, 0, 11)
    diff = []
    for h in hlist:
        tlist = np.arange(0, 10, h)

        x_analytic = xi * np.cos(tlist) + vi * np.sin(tlist)
        xlist = []

        for t in tlist:
            xlist.append(xi)
            xi, vi = xi + h * vi, vi - h * xi

        difference = np.max(x_analytic - np.array(xlist))
        diff.append(difference)


    plt.figure()
    plt.loglog(hlist, diff, label = "analytic numerical diff")
    plt.legend()
    plt.savefig('analytic-numerical')


# Problem 4, numerical evolution of total energy

def energy(xi, vi, h):
    '''
    This function computes the total energy (E = v^2 + x^2) and plots E vs time.
    '''
    Elist = []
    tlist = np.arange(0, 10, h)
    for t in tlist:
        xi, vi = xi + h * vi, vi - h * xi
        E = vi ** 2 + xi ** 2
        Elist.append(E)
    plt.figure()
    plt.plot(tlist, Elist, label = "Energy")
    plt.legend()
    plt.savefig('energy.pdf')


# Problem 5, implicit Euler comparison

def implicit(xi, vi, h):
    '''
    This function uses the implicit Euler method and evaluates it numerically.
    The global error and energy calculations are compared to those given by the
    explicit Eulers method.
    '''
    x_explicit = []
    v_explicit = []
    x_implicit = []
    v_implicit = []
    tlist = np.arange(0, 10, h)

    for t in tlist:
        x_explicit.append(xi)
        v_explicit.append(vi)
        xi, vi = xi + h * vi, vi - h * xi 

    for t in tlist:
        x_implicit.append(xi)
        v_implicit.append(vi)

        xi1 = (xi + h * vi)/(1 + h ** 2)
        vi1 = (vi - h * xi - h * vi)/(1 - h)
        xi = xi1
        vi = vi1

    plt.figure()
    plt.plot(tlist, x_explicit, 'b-', label = "x explicit")
    plt.plot(tlist, v_explicit, 'g-', label = "v explicit")
    plt.plot(tlist, x_implicit, 'b--', label = "x implicit")
    plt.plot(tlist, v_implicit, 'g--', label = "v implicit")
    plt.legend()
    plt.savefig('explicit_implicit.pdf')


    E_implicit = []
    E_explicit = []
    tlist = np.arange(0, 10, h)
    for t in tlist:
        xi, vi = xi + h * vi, vi - h * xi
        E_exp = vi ** 2 + xi ** 2
        E_explicit.append(E_exp)
    for t in tlist:
        xi1 = (xi + h * vi)/(1 + h ** 2)
        vi1 = (vi - h * xi - h * vi)/(1 - h)
        E_imp = vi ** 2 + xi ** 2
        E_implicit.append(E_imp)
        xi = xi1
        vi = vi1

    plt.figure()
    plt.plot(tlist, E_implicit, label = "Energy implicit")
    plt.plot(tlist, E_explicit, label = "Energy explicit")
    plt.legend()
    plt.savefig('Energy_exim.pdf')



def main():

    parser = argparse.ArgumentParser(description='something')

    parser.add_argument('-a', '--analytic', 
        type=float, metavar=('XI', 'VI', 'H'), nargs=3, help='something')

    args = parser.parse_args()

    if args.analytic is not None:
        analytic(*args.analytic)


    spring(0, 5, .1)
    analytic(0, 5, .1)
    truncation(0, 5, .1)
    energy(0, 5, .1)
    implicit(0, 5, .1)

if __name__ == '__main__':
    main()
