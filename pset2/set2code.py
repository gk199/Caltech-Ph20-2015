import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import pi
import scipy.integrate as sci
from scipy.integrate import quad
from scipy.special import erf

# Physics 20 Assignment 2

# Problem 2, extended trapezoid rule

def integrate_trap(func, a, b, N):
    '''
    This function integrates the function 'func' using the extended trapezoid
    rule. a and b are the extrema of integration and N is the number of
    subintervals used.
    '''
    a = float(a)
    b = float(b)
    hn = (b - a) / N
    n = np.arange(a, b, hn)
    n = map(func, n)
    function = n[1:] + n[:-1]
    trap = (np.sum(function)) * hn / 2
    return trap

# Problem 3, extended Simpsons formula

def integrate_Simpson(func, a, b, N):
    '''
    This function integrates the function 'func' using the extended Simpson's
    formula. a and b are the extrema of integration and N is the number of
    subintervals used.
    '''
    a = float(a)
    b = float(b)
    hn = (b - a) / N
    n = np.arange(a, b, hn)
    n = map(func, n)
    fa = func(a)
    fb = func(b)
    n4 = n[1:][0::2]                                 # to multiply by 4
    n2 = n[2:][0::2]                                 # to multiply by 2
    simpson = (np.sum(4 * n4 + 2 * n2) + fa + fb) * (hn / 3)
    return simpson

# Problem 4, compare accuracy, plot

def error_plot(func, a, b, value, ni, nf):
    '''
    This function will evaluate and plot the error of the Simpsons approximation
    and the trapezoid approximation functions for various values of N (number of
    subintervals). ni and nf are the input values for the starting and final
    values of n (where n are the inputs to simpson and trapezoid approximations)
    '''
    trap_error = []
    simpson_error = []
    Nlist = np.logspace(ni, nf)
    Nlist = 2 * np.round(0.5 * Nlist)                  # integers to plot
    for nval in Nlist:
        Simpson = integrate_Simpson(func, a, b, nval)
        Trap = integrate_trap(func, a, b, nval)
        S_error = abs(value - Simpson)
        T_error = abs(value - Trap)
        simpson_error.append(S_error)
        trap_error.append(T_error)
    plt.loglog(Nlist, simpson_error, label = "Simpson error")
    plt.loglog(Nlist, trap_error, label = "Trapezoid error")
    plt.legend()
    plt.show()

# Problem 5, determine relative accuracy

def integrate_accuracy(func, a, b, acc, maxiter=20):
    '''
    This function integrates the function "func" to a specified accuracy level,
    "acc". This is done by evaluating Simpson's formula for N = N0, 2 * N0,
    4 * N0... until the relative difference between the approximations is less
    than the accuracy specified in the input.
    '''
    exp = 1
    N0 = 1
    for _ in range(maxiter):
        first = integrate_Simpson(func, a, b, ((2 ** exp) * N0))
        exp += 1
        second = integrate_Simpson(func, a, b, ((2 ** exp) * N0))
        rel_diff = abs((first - second) / first)
        if rel_diff < acc:
            return ((2 ** exp) * N0)


def func(x):
    '''
    This is the function that will be used as arguments by integrate_Simpson and
    integrate_trap functions.
    '''
    function = math.exp(x)
    return function

def main():
    # Problem 6, comparison to integrate quad and romberg functions
    x, y = sci.quad(func, 0, 1)
    print x
    print "Quad function integral"
    print sci.romberg(func, 0, 1)
    print "Romberg function integral"


    # print integrals computed with trap and Simpson functions
    print integrate_trap(func, 0, 1.0, 100)
    print "Trapezoid integral"
    print integrate_Simpson(func, 0, 1.0, 100)
    print "Simpson integral"


    # make error plot function
    error_plot(func, 0, 1.0, 1.7182818284590452354, 1, 6)

    # accuracy function
    print integrate_accuracy(func, 0, 1.0, 0.0001)
    print "Accuracy function"

if __name__ == '__main__':
    main()
