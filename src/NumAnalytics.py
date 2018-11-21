'''
Created on Oct 30, 2018

@author: Pavel Shavarchov
'''
from numpy.lib.polynomial import poly1d, polyval,polyder
from builtins import str
import re
import numpy as np
from numpy.ma.core import arange

class Polynom(object):
    @staticmethod
    def parsePoly(expr,var = r'[xX]'):
        """ parse Polynom from text, for example: "+10 +5.3x^2 -55 x**4" is converted to the poly series [1,0,5.3,0,-45]"""
        expr = expr.replace(' ','').replace('-','+-').replace('^','**').split('+');
        pattern = re.compile(var)
        terms = [pattern.split(term) for term in expr];
        terms = [[term[0],term[1].replace('**','') if len(term)>1 else '0'] for term in terms]
        terms = [[item + '1' if (item == '' or item == '-') else item for item in term] for term in terms]
        c_pow = {}
        degree = 1
        for term in terms:
            term = [eval(term[0]),int(term[1])]
            if term[1]>degree:
                degree = term[1]
            if c_pow.get(term[1])==None:
                c_pow[term[1]] = 0
            c_pow[term[1]]+= term[0]
        return [c_pow[degree-i] if c_pow.get(degree-i) else 0 for i in range(degree+1)]
    
    
    def __init__(self,expr):
        if isinstance(expr, Polynom):
            expr = expr.polynom
        if isinstance(expr, str):
            expr = Polynom.parsePoly(expr)
        self.polynom = poly1d(expr)
        
    def __str__(self):
        return str(self.polynom);
    
    def eval(self,x):
        """calculates and returns p(x)"""
        return polyval(self.polynom,x)
    
    def derive(self):
        """returns a Polynom class member """
        return Polynom(polyder(self.polynom))
    
    def __eq__(self,other):
            return self.polynom == other.polynom
     
    def getRootsByHalf(self,totalZone=(-5,5),zoneCount=89,maxError=0.01,derived = False, **kwargs):
        
        def testRoot(root):
            return abs(self.eval(root)) < maxError
        
        def getRoot(zone):
            fa,fb = self.eval(zone[0]),self.eval(zone[1])

            if(fa*fb<0):
                return solveRoot(zone,fa,fb)
            else:
                return None
            
        def solveRoot(zone,fa,fb):
            m = (zone[0]+zone[1])/2
            fm = self.eval(m)
            if abs(fm) < maxError:
                return m;
            elif fa*fm<0:
                return solveRoot((zone[0],m), fa, fm)
            else:
                return solveRoot((m,zone[1]), fm, fb)
                
        def getZones():
            step = (totalZone[1] - totalZone[0])/zoneCount
            temp = arange(totalZone[0],totalZone[1]+1,step)
            return [(temp[i],temp[i+1]) for i in range(len(temp)-1)]
        
        Zones = getZones()
        roots = []
        for zone in Zones:
            root = getRoot(zone)
            if root:
                roots.append(root)
        if derived:
            return roots;
        elif len(roots)<self.polynom.order:
            roots.extend([root for root in self.derive().getRootsByHalf(derived=True) if testRoot(root)])
            roots.sort()
        return roots
                
        
class Matrix(np.matrix):
    def __init__(self,*arg):
        super().__init__()
        
    def decomposeDLU(self):
        """
        returns a tuple (d,l,u);
        d = direct/ main axis of the matrix: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[1,0,0],[0,5,0],[0,0,9]])
        l = lower matrix triangle: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[0,2,3],[0,0,6],[0,0,0]])
        u = upper matrix triangle: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[0,0,0],[4,0,0],[7,8,0]])
        (d+l+u)= m 
        """
        rows, cols = self.shape
        if rows!=cols:
            return None;
        data = self.tolist()
        direct = Matrix([[data[i][j] if i==j else 0 for j in range(cols)] for i in range(rows)])
        lower = Matrix([[data[i][j] if j>i else 0 for j in range(cols)] for i in range(rows)])
        upper = Matrix([[data[i][j] if j<i else 0 for j in range(cols)] for i in range(rows)])
        return (direct, lower, upper)
    
    def interationSolver(self,result=None,g=None,h=None,startingGuess=None,maxError=0.01):
        matrixDegree = self.shape[0]
        startingGuess = Matrix([[0] for _ in range(matrixDegree)]) if startingGuess==None else startingGuess
        result = Matrix([[i] for i in result]) if not isinstance(result, Matrix) else result
        
        def iteration():
            i,currGuess=0,startingGuess
            nextGuess = g*currGuess + h*result
            
            
        
            
        
if __name__ == '__main__':
#     p1 = Polynom("x^2 -2")
#     print(p1)
#     print('-----------')
#     print(p1.derive())
#     print('-----------')
#     print(p1)
#     print('-----------')
#     print(p1.getRootsByHalf())
#     print('-----------')
    m1 = Matrix('[1,2,3;4,5,6;7,8,9]')
#     [print(x,'\n') for x in m1.decomposeDLU()]
#     print(sum(m1.decomposeDLU()))
print(m1.interationSolver([1,1,1]))
