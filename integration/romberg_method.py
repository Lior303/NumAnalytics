# module_romberg
'''
I , nP = romberg(func,a,b,tol=1.0e-6).
Romberg integration of f(x) from x = a to bselfself.
Return the integral and the number of panelsself.

'''
import numpy as np
from recursive_trapezoid import trapezoid


def romberg(f, a, b, tol=1.0e-6):

    def richardson(r, k):
        for j in range(k-1, 0, -1):
            const = 4.0**(k-j)
            r[j] = (const*r[j+1]-r[j])/(const-1.0)
        return r

    r = np.zeros(21)
    r[1] = trapezoid(f, a, b, 0.0, 1)
    r_old = r[1]
    for k in range(2, 21):
        r[k] = trapezoid(f, a, b, r[k-1], k)
        r = richardson(r, k)
        if abs(r[1]-r_old) < tol*max(abs(r[1]), 1.0):
            return r[1], 2**(k-1)
        r_old = r[1]
    print("not converge")

if __name__=="__main__":
    try:
        import math
        def f(x): return (2.0*(x**2)*math.cos(x**2))
        I, n = romberg(f, 0, (math.pi)**0.5)
        print(f"""
        integral = {I}
        numEvals = {n}
        """)
    except:
        pass

