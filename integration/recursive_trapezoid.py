# module_trapezoid
'''
Inew - trapezoid (func ,a,b,Iold,k).
Recursive trapezoid rule:
old=Integral of f(x) from x = a to b
computed by trapezoid rule with 2^(k-1) panelsself.
Inew = same integral computed with 2^k panels.
'''


def trapezoid(funciton, a, b, Iold, k):
    if k == 1:
        Inew = (funciton(a)+funciton(b))*(b-a)/2.0
    else:
        n = 2**(k-2)
        h = (b-a)/n
        x = a+h/2.0
        sum = 0.0
        for i in range(n):
            sum = sum+funciton(x)
            x = x+h
        Inew = (Iold+h*sum)/2.0
    return Inew
