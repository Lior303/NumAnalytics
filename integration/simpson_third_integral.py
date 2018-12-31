def simpson_third(f,dom,n=2):
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
    try:
        from numpy import log as ln
        i=lambda x: x*ln(x) -x
        print(f"""integral of ln(x):
        using simpson:     {simpson_third(lambda x:ln(x),(1,3),n=2)}
        analitic method:   {i(3)-i(1)}
        """)
    except:
        pass
    