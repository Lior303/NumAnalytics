import numpy
from matrix.gaussian_elimination_method import gaussian_eliminate_result_adapter as gauss

# url = https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation

def devided_diff(args,method=None):
    k = len(args)
    if (k == 0): 
        return method(args) if method!=None else args[1]
    else:
        return (devided_diff(args[1:], method) - devided_diff(args[:-1], method)) / (args[-1:] - args[:1])
     

class Point:
    def __init__(self,tup):
        self.x = tup[0]
        self.y = tup[1]
    def __repr__(self):
        return f"(x:{self.x},y:{self.y})"

def cubic_spline(data=[(2.5,0.5),(1,1),(3,0.25),(4,0.125),(5,0.0625)] , solver = gauss ,**kwargs):
    data = [Point(p) for p in data]
    data.sort(key=lambda elem:elem.x)
    
    n = len(data) # size of matrix
    
    h = [None] + [abs(data[i].x - data[i-1].x) for i in range(1,n)] # array of distances
    
    def create_matrix(bounds = None):
        dg = [2 for _ in range(n)] #diag of matrix
        lmda = ([0] if not bounds else [1]) + ([(h[i+1])/(h[i]+h[i+1]) for i in range(1,n-1)])
        mu = [(h[i])/(h[i]+h[i+1]) for i in range(1,n-1)] + ([0] if not bounds else [1])
        matrix = numpy.diag(dg) + numpy.diag(lmda,k=1) + numpy.diag(mu, k=-1)
        return matrix
    
    def create_d(bounds = None):
        d0 = ([0] if not bounds else [(h[1]/6)*(devided_diff(data[:2]) - bounds[0])])
        dn = ([0] if not bounds else (h[n]/6)*(devided_diff(data[-2:]) - bounds[1]))
        return d0 + [devided_diff(data[i-1:i+1]) for i in range(1,n-1)] + dn
    
    matrix = create_matrix(**kwargs)
    
    return matrix

if __name__ == "__main__":
#     lst = [1,2,3]
#     new = lst[:1]
#     other = lst[-1:]
#     print(new, other)
    print(cubic_spline())