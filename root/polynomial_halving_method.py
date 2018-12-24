'''
Created on Nov 26, 2018

@author: Pavel
'''

import numpy as np
import re
from numpy.core.multiarray import arange

class Polynom(np.poly1d):
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
        if isinstance(expr, str):
            expr = Polynom.parsePoly(expr)
        super().__init__(expr)

    def eval(self,x):
        """calculates and returns p(x)"""
        return np.polyval(self,x)

    def derive(self):
        return Polynom(np.polyder(self))

    def getRootsHalvingMethod(self,totalZone=(-5,5),maxError=0.01,repeatForDerived = True, **kwargs):

        def testRoot(root):
            return abs(Polynom.eval(self,root)) < maxError

        def getRoot(zone, fa=None, fb=None):
            a,b = zone
            if(not fa or not fb):
                fa,fb = Polynom.eval(self,a),Polynom.eval(self,b)
                if(abs(fa)<maxError):
                    return a
                if(abs(fb)<maxError):
                    return b
            if(fa*fb<0):
                m = (a+b)/2
                fm = Polynom.eval(self,m)
                print('*****CHECKING', ('Original' if repeatForDerived else 'Derived') , ', zone :',zone, ', (fa,fm,fb)=',(fa,fm,fb))
                if abs(fm) < maxError:
                    return m;
                elif fa*fm<0:
                    return getRoot((a,m), fa=fa, fb=fm)
                else:
                    return getRoot((m,b), fa=fm, fb=fb)
            else:
                print('NOT CHECKING ' , ('Original' if repeatForDerived else 'Derived') , ', zone :',zone, ', (fa,fb)=',(fa,fb))
                return None


        def getZones(zoneCount=25):
            step = (totalZone[1] - totalZone[0])/zoneCount
            temp = arange(totalZone[0],totalZone[1]+1,step)
            return [(temp[i],temp[i+1]) for i in range(len(temp)-1)]

        Zones = getZones(**kwargs)
        roots = []
        for zone in Zones:
            root = getRoot(zone)
            if root:
                roots.append(root)
        if(len(roots)<self.order and repeatForDerived):
            roots.extend([root for root in Polynom.getRootsHalvingMethod(Polynom.derive(self),repeatForDerived=False) if testRoot(root)])
            roots.sort()
        return roots

if __name__ == '__main__':
    p2 = np.poly1d([1,1,1,-2])
    print(p2)
    print(Polynom.getRootsHalvingMethod(p2,totalZone=(-5,5),zoneCount=25))
