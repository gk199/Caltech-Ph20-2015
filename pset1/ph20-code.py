import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import pi

# Physics 20 Assignment 1

def trigfunc(fx, fy, Ax, Ay, phi, dt, N):
    '''
    This function computes sequences of three trig functions and outputs 
    the sequences to ASCII files.
    '''
    def t_func(n):
        return dt * n
    def x_func(t):
        return Ax * math.cos(2 * pi * fx * t)
    def y_func(t):
        return Ay * math.sin(2 * pi * fy * t + phi)
    def z_func(X, Y):
        return X + Y

    T = map(t_func, range(N + 1))
    X = map(x_func, T)
    Y = map(y_func, T)
    Z = map(z_func, X, Y)

    return (T, X, Y, Z)

def trigfunc2(fx, fy, Ax, Ay, phi, t, N):
    '''
    This function computes sequences of three trig functions and outputs 
    the sequences to ASCII files.
    '''
    n = np.arange(N +1)
    T = t * n
    X = Ax * np.cos(2 * pi * fx * T)
    Y = Ay * np.sin(2 * pi * fy * T + phi)
    Z = X + Y
    A = 2 * Ax * np.cos(pi * (fx + fy) * T) * np.cos(pi * (fx - fy) * T)

    np.savetxt('x_datafile', X, delimiter = " ")
    np.savetxt('y_datafile', Y, delimiter = " ")
    np.savetxt('z_datafile', Z, delimiter = " ")
    np.savetxt('TESTFILE', A, delimiter = " ")

    return (T, X, Y, Z, A)

def main():
    fx = 2
    fy = 7
    Ax = 5
    Ay = 5
    phi = 10
    t = 0.002
    N = 500

    T, X, Y, Z, A = trigfunc2(fx, fy, Ax, Ay, phi, t, N)
    f = open('trigfile.txt', 'w')
    for i in range(len(X)):
        f.write("{} {}\n".format(X[i], Y[i], Z[i]))
    f.close()

    plt.figure()
    plt.plot(T, X)
    plt.savefig('xplot.png')

    plt.figure()
    plt.plot(T, Y)
    plt.savefig('yplot.png')

    plt.figure()
    plt.plot(T, Z)
    plt.savefig('zplot.png')

    plt.figure()
    plt.plot(X, Y)
    plt.savefig('xyplot.png')

    plt.figure()
    plt.plot(T, A)
    plt.savefig('TESTPLOT.png')


if __name__ == '__main__':
    main()