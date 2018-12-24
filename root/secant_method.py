def secant_method(f, x0, x1, epsilon=10**-4, nMax=100):
    """
    secant method to calculate x's (roots) of a function
    :param f: the function
    :param x0: start value
    :param x1: start value
    :param epsilon: fault degree allowed
    :param nMax: maximum of iterations
    """
    n=1
    while n<=nMax:
        x2 = x1 - f(x1) * ((x1 - x0) / float(f(x1) - f(x0)))
        if (abs(f(x2))<epsilon):
            print("\nThe root is: {}".format(x2))
            return x2
        else:
            print("x0: {}, x1: {}".format(x0, x1))
            x0=x1
            x1=x2
    return False

if name__ == "__main__":
    print("Enter a function f(x): ")
    func=eval("lambda x: " + input(""))
    print("Enter start values: x0 and x1")
    secant_method(func, float(input("x0=")), float(input("x1=")))

"""
Takes a function f, start values [x0,x1], tolerance value(optional) epsilon and
max number of iterations(optional) nMan and returns the root of the equation
using the secant method.

The function f must be continuous in the section [x0, x1].
Secant method does not uses derivative of function f, therefore if the function f have a complicated
derivative or if the derivative is to complex the secant method will be converge faster
than the newton-raphson method.

f(x1) - f(x0) must be different that zero.
"""