import numpy
from matrix.gaussian_elimination_method import gaussian_eliminate_result_adapter as gauss

# url = https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation

def devided_diff(args):
    """calculates the dividen difference recurcively, url: https://en.wikipedia.org/wiki/Divided_differences """
    k = len(args)
    if (k == 1): 
        arg = args[0]
        return arg.y
    else:
        return (devided_diff(args[1:]) - devided_diff(args[:-1])) / (args[-1:][0].x - args[:1][0].x)
     

class Point:
    def __init__(self,tup):
        self.x = tup[0]
        self.y = tup[1]
    def __repr__(self):
        return f"(x:{self.x},y:{self.y})"


def route_function(ranges,functions):
    """given a list of ranges and a list of functions return a function f(x) that if x in ranges[i] return functions[i](x)
    """
    def evaluate(x):
        for i in range(len(ranges)):
            if(ranges[i][0]<=x and x<=ranges[i][1]):
                return functions[i](x)         
    return evaluate

def cubic_spline(data , solver = gauss ,**kwargs):
    """given a list of tuples representing (x,y) point create a "smooth" function where the first and second derivatives are continuous along the graph
    possible kwargs: 
        bounds= 2 item tuple containing edge case first derivatives, example bounds=(-5,5) for the dataset [(x=1,y=?),(x=2,y=?),....,(x=10,y=?)] the resulting smooth functions f'(1)=-5, f'(10)=5
    """
    def create_h():
        """creates an array h that each h[i]=x[i]-x[i-1]"""
        return [None] + [abs(data[i].x - data[i-1].x) for i in range(1,n)] # array of distances
    
    def create_matrix(bounds = None):
        """
        creates the matrix  [[    2,  lm[0],      0,      0,        0]
                             [mu[1],      2,  lm[1],      0,       ,0]
                             [    0,  mu[2],      2,       ,       ,0]
                             [    0,      0,       ,      2,  lm[n-1]]
                             [    0,      0,      0,  mu[n],       2]]
        """ 
        dg = [2 for _ in range(n)] #diag of matrix
        lm = ([0] if not bounds else [1]) + ([(h[i+1])/(h[i]+h[i+1]) for i in range(1,n-1)])
        mu = [(h[i])/(h[i]+h[i+1]) for i in range(1,n-1)] + ([0] if not bounds else [1])
        matrix = numpy.diag(dg) + numpy.diag(lm,k=1) + numpy.diag(mu, k=-1)
        return numpy.matrix(matrix)
    
    def create_d(bounds = None):
        """creates the results matrix d where each d[i] = 6*devided_difference(x[i-1],x[i],x[i+1] except for eadge cases.
        bounds represent the known first derivative of the edge cases, and are calculated accordingly 
        """
        d0 = ([0] if not bounds else (devided_diff(data[:2]) - bounds[0])/h[1])
        dn = ([0] if not bounds else (bounds[1] - devided_diff(data[-2:]))/h[n-1])
        d = [d0] + [devided_diff(data[i-1:i+2]) for i in range(1,n-1)] + [dn]
        d = [6*x for x in d]
        return d
    
    def create_polynoms(m):
        """create a list containing polynomials for each range of points, ie: c[i] is the part function for calculating f(x) for x[i-1]<x<x[i]"""
        def func(roots):
            """given n roots x1,x2...xn creates the polynom (x-x1)*(x-x2)....*(x-xn)
            """
            return numpy.poly1d(numpy.poly(roots))
        
        def create_c(i):
            """given index i create lagrange polynomial complient with found deriveatives m[], returns a numpy poly1d
            """
            prod1 = (m[i-1]*(-1*func([data[i].x]))**3)/(6*h[i])
            prod2 = (m[i]*(func(data[i-1].x))**3)/(6*h[i])
            prod3 = (data[i-1].y - (m[i-1]*(h[i]**2))/6) * (-1*func([data[i].x])/h[i])
            prod4 = (data[i].y - (m[i]*(h[i]**2))/6) * (func(data[i-1].x) / h[i])
            return prod1 + prod2 + prod3 + prod4
        
        return [None] + [create_c(i) for i in range(1,n)]  
                    
    data = [Point(p) for p in data]
    data.sort(key=lambda elem:elem.x)
    n = len(data)
    h= create_h()
    matrix = create_matrix(**kwargs)
    d = create_d(**kwargs)
    d = [[x] for x in d]
    m = solver(matrix,d)
    c = create_polynoms(m)
    
    ranges = [(data[i].x,data[i+1].x) for i in range(n-1)]
    functions = c[1:]
    
    return route_function(ranges,functions) 

def graph(f, points = None, precision = 0.001):
    try:
        import matplotlib.pyplot as pyplot
    except:
        print("cannot import matplotlib")
        return
    getx = lambda elem:elem[0]
    rng = (getx(min(data, key = getx)),getx(max(data, key = getx)))
    x=numpy.arange(rng[0],rng[1]+precision,precision)
    y=[f(i) for i in x]
    pyplot.plot(x,y)
    if points!=None:
        px = [i[0] for i in points]
        py = [i[1] for i in points]
        pyplot.scatter(px, py)
    pyplot.show()


if __name__ == "__main__":
    data = [(0,0),(1,0.5),(2,2),(3,1.5)]
    cubic = cubic_spline(data = data,bounds=[0.2,-1])
    graph(cubic,points=data)

