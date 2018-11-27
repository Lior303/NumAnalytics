def derive(f):
    """
    This function return the numerial calculated derived function of f.
    :param f: the function
    :return: derived function
    """
    h = 10**-10
    return lambda x: (f(x + h) - f(x))/float(h)

def newtonraphson_method(f, x0, epsilon=10**-4, nMax=100):
    """
    newtonraphson_method to calculate x's (roots) of a function
    :param f: the function
    :param x0: start value
    :param epsilon: fault degree allowed
    :param nMax: maximum of iterations
    """
    n = 1
    f_ = derive(f)
    while n <= nMax:
        if (f_(x0)==0):
            print("Error!, division by zero.")
            return
        x1 = x0 - (f(x0) / f_(x0))
        print("x0: {}, x1: {}".format(x0, x1))
        if (x1-x0<epsilon):
            print("\nThe root is: {}".format(x1))
            return x1
        else:
            x0=x1
    return False

print("Enter a function f(x): ")
func=eval("lambda x: " + input(""))
print("Enter x0 start value: ")
x0=float(input())
newtonraphson_method(func, x0)

"""
Takes a function f, initial value x0, tolerance value(optional) epsilon and
max number of iterations(optional) nMax and returns the root of the equation
using the newton-raphson method.

In this method the derive function of f must be defined, f must be continuous.
if the function f have a complicated derivative or if the derivative is to complex, this method
will not converge, or converge very slow.

This method will not work for every function f. the derived function of f must be defined.
And the derived function of f must be different that zero.
"""