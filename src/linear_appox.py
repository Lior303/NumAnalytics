def linear_approximation(x1, x2, y1, y2, xf):
    sum1 = ((y2-y1)/float(x2-x1))*xf
    sum2 = (y1*x2 - y2*x1)/float(x2-x1)
    return sum1 + sum2

"""
linear approximation: using x1, x2, y1, y2 and xf ---> the x value of the unknown yf
the function return the linear approximation.
"""