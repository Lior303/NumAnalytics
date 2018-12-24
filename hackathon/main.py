'''
Created on Dec 3, 2018

@author: Pavel
'''
import numpy as np
from matrix.matrix_iteration import Matrix, addKwargs
from  matrix.gaussian_elimination_method import gaussian_eliminate_result_adapter
import math

def getDMatrix():
    c = 0.6844
    k=3.23691625
    u = 0.003733
    math.e
    def getRadius(i,j):
        radius = [[150,180,180,206.155],[180,150,206.155,180],[180,206.155,150,180],[206.155,180,180,150]]
        return radius[i][j]
    
    def getD(i,j):
        return (c*(1+k*150)*math.e**(-u*getRadius(i, j)))/getRadius(i, j)**2
   
    result = [[getD(i,j) for j in range(4)] for i in range(4)]
    return np.matrix(result)  

def CalcC(solver):
    M = Matrix([[x] for x in [1250,1550,1100,1400]])
    D = getDMatrix()
    print("M:\n",M)
    print("D:\n",D)
    return solver(D,M)
    
if __name__ == '__main__':
    solver = addKwargs(Matrix.iterGaussSeidel,n=50)
#     solver = gaussian_eliminate_result_adapter
    print("vector c: ", CalcC(solver).tolist())
    
            
            

