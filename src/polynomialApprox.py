import numpy as np
# import  gaussian_elimination_method as func

def polynomial_approximation(dict, matrixSolver = gaussian_eliminate_result_adapter):
    def createMatrix():
        size = len(dict.keys())
        return np.matrix([[x ** i for i in range(size - 1, -1, -1)] for x in dict.keys()])

    def createResultsVector():
        return np.matrix([[y] for y in dict.values()])

    def unpackVector(vector):
        return vector.flatten()
    
    matrixA , vectorB = createMatrix(), createResultsVector()
    vectorX = matrixSolver(matrixA,resultB)
    
    return np.poly1d(vectorX)

def gaussian_eliminate_result_adapter(A,b):
    return func.gaussian_eliminate_result(np.append(A,b, axis=1))

print(polynomial_approximation({1:1, 10:0.1, 20:0.05}))