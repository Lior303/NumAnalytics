def simpsons_third(f,dom,n):
    """
    f = callable that returns a single numeric value, the function that we want to find the integral of.
    dom = the integral domain
    n = number of chunks to perform the integration on. must be positive and devisable by 2.
    """
    a,b = dom
    if n%2!=0: n+=1
    if b<a: a,b = b,a
    h = (b-a)/n
    x = lambda i: a+i*h
    sum = f(a) + f(b)
    for i in  range(1,n):
        sum+= 4*f(x(i)) if i%2!=0 else 2*f(x(i))
    return h*sum/3


if __name__=="__main__":
    x = simpsons_third(lambda x: x**3 -3, (0,2), 1)
    print(x)