import numpy
import matplotlib.pyplot as pyplot
from matrix.gaussian_elimination_method import gaussian_eliminate_result_adapter as gauss

# url = https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation

def devided_diff(args):
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
    def evaluate(x):
        for i in range(len(ranges)):
            if(ranges[i][0]<=x and x<=ranges[i][1]):
                return functions[i](x)         
    return evaluate

def cubic_spline(data , solver = gauss ,**kwargs):
    def create_h():
        return [None] + [abs(data[i].x - data[i-1].x) for i in range(1,n)] # array of distances
    
    def create_matrix(bounds = None):
        dg = [2 for _ in range(n)] #diag of matrix
        lmda = ([0] if not bounds else [1]) + ([(h[i+1])/(h[i]+h[i+1]) for i in range(1,n-1)])
        mu = [(h[i])/(h[i]+h[i+1]) for i in range(1,n-1)] + ([0] if not bounds else [1])
        matrix = numpy.diag(dg) + numpy.diag(lmda,k=1) + numpy.diag(mu, k=-1)
        return numpy.matrix(matrix)
    
    def create_d(bounds = None):
        d0 = ([0] if not bounds else (devided_diff(data[:2]) - bounds[0])/h[1])
        dn = ([0] if not bounds else (bounds[1] - devided_diff(data[-2:]))/h[n-1])
        d = [d0] + [devided_diff(data[i-1:i+2]) for i in range(1,n-1)] + [dn]
        d = [6*x for x in d]
        return d
    
    def create_polynoms(m):
        def func(roots):
            return numpy.poly1d(numpy.poly(roots))
        
        def create_c(i):
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

def graph(f, rng, precision = 0.1):
    print(*rng)
    x=numpy.arange(*rng,precision)
    y=[f(i) for i in x]
    pyplot.plot(x,y)
    pyplot.show()

if __name__ == "__main__":
    data = [(0,0),(1,0.5),(2,2),(3,1.5)]
    cubic = cubic_spline(data = data,bounds=[0.2,-1])
    getx = lambda elem:elem[0]
    total_range = (getx(min(data, key = getx)),getx(max(data, key = getx)))
    graph(cubic,total_range)