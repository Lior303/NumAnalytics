'''
Created on Oct 30, 2018

@author: Pavel Shavarchov
'''
import numpy as np
from numpy.random.mtrand import random_sample

def addKwargs(func,**kwargs):
    return lambda *args,**newkwargs : func(*args,**{**kwargs,**newkwargs})

class Matrix(np.matrix):
    def decompose(self,*selections):
        """
        D = direct/ main axis of the matrix: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[1,0,0],[0,5,0],[0,0,9]])
        L = lower matrix triangle: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[0,2,3],[0,0,6],[0,0,0]])
        U = upper matrix triangle: ([[1,2,3],[4,5,6],[7,8,9]]) => ([[0,0,0],[4,0,0],[7,8,0]])
        (d+l+u)= m
        LU = L+U
        DL = D+L
        """
        rows, cols = self.shape
        if rows!=cols:
            return None;
        data = self.tolist()
        methods = {
            'D':(lambda:Matrix([[data[i][j] if i==j else 0 for j in range(cols)] for i in range(rows)])),
            'U':(lambda:Matrix([[data[i][j] if i<j else 0 for j in range(cols)] for i in range(rows)])),
            'L':(lambda:Matrix([[data[i][j] if i>j else 0 for j in range(cols)] for i in range(rows)])),
            'LU':(lambda:Matrix([[data[i][j] if i!=j else 0 for j in range(cols)] for i in range(rows)])),
            'DL':(lambda:Matrix([[data[i][j] if i>=j else 0 for j in range(cols)] for i in range(rows)])),
            }
        return (methods[select]() if select in methods else None for select in selections)
    
    def guessError(self,result,guess):
            return abs(result - (self * guess)).max()
    
    def iterSolver(self,g,h,result=None,startingGuess=None,maxError=0.001,**kwargs):
        """
        performs x{i+1} = g*x{i} + h*b, stops when reaches n = max iteration or reaches valid guess 
        """
        matrixDegree = self.shape[0]
        startingGuess = Matrix([[0] for _ in range(matrixDegree)]) if startingGuess==None else startingGuess
        result = Matrix([[i] for i in result]) if not isinstance(result, np.matrix) else result
        
        def guessError(guess):
            return abs(result - (self * guess)).max()
        
        def iteration(n=25):                  
            currGuess=startingGuess
            i=1
            err = maxError
            while(i<=n):
                nextGuess = g*currGuess + h*result
                if(abs(nextGuess - currGuess).max()<err):
                    currGuess = nextGuess
                    if(guessError(currGuess)<maxError):
                        break
                    else:
                        print("close, but not enough; decreasing range")
                        err = err/10
                currGuess = nextGuess
                i+=1
                print("guess #{}: {}".format(i-1,currGuess.tolist()))
            print("done in iteration number : " , i-1)
            return currGuess
             
        guess = iteration(**kwargs)
        print("guess error:",guessError(guess),", result guess:\n",guess,'')
        return guess
    
    def iterJacobi(self,result,**kwargs):
        lu,d = Matrix.decompose(self,'LU','D')
        dInver = d**-1
        g = -dInver*lu
        h = dInver
        return Matrix.iterSolver(self, g, h, result,**kwargs)

    def iterGaussSeidel(self,result,**kwargs):
        dl,u = Matrix.decompose(self,'DL','U')
        dlInver = dl**-1
        g = -dlInver*u
        h = dlInver
        return Matrix.iterSolver(self, g, h, result,**kwargs)
    
    def iterSOR(self,result,w=None,**kwargs):
        w = 2*random_sample() if (w==None or w>2 or w<=0) else w
        d,l,u = Matrix.decompose(self,'D','L','U')
        dwlInver = (d+w*l)**-1
        g = dwlInver * ((1-w)*d -w*u)
        h = w * dwlInver
        print("w: ", w)
        return Matrix.iterSolver(self, g, h, result, **kwargs)
        
if __name__ == '__main__':
    m1 = np.matrix('[2,1;5,7]')
    print(Matrix.iterJacobi(m1, [11,13],n=25))
#     print(m1.iterJacobi([11,13],n=25))
#     print(m1.iterSOR([11,13],n=100))


