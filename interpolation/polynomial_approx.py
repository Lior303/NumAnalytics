import numpy as np
from  gaussian_elimination_method import gaussian_eliminate_result_adapter
from matrix import Matrix, addKwargs
from polynomial_halving_method import Polynom

def polynomial_approximation(dict, matrixSolver = gaussian_eliminate_result_adapter):
    """
    :param dict: the dictionary that was given
    :return: result vector as a polynom.
    """
    def createMatrix():
        """
        create the matrix
        :return: the matrix from the dictionary
        """
        size = len(dict.keys())
        return np.matrix([[x ** i for i in range(size - 1, -1, -1)] for x in dict.keys()])

    def createResultsVector():
        """
        :return: the resut vector
        """
        return np.matrix([[y] for y in dict.values()])

#     def unpackVector(vector):
#         return vector.flatten()

    matrixA , vectorB = createMatrix(), createResultsVector()
    vectorX = matrixSolver(matrixA,vectorB)
    if isinstance(vectorX, np.matrix):
        vectorX = vectorX.flatten().tolist()[0]
    return np.poly1d(vectorX)

if __name__ == '__main__':
#     solver = addKwargs(Matrix.iterSOR,n=100,w=1.5)
    p1 = polynomial_approximation({2:-3.5, 3:1.25, 6:0.05},matrixSolver=gaussian_eliminate_result_adapter)
    p1 = Polynom(p1)
    print("f(3.83) = ", p1.eval(3.83))


"""
polynomial approximation. calculate and return the polynom from the polynomial approximation of a known dictionary (the table)
first, crate the matrix using the ductionary, then create resut vector ---> it will be the values of the dictionary.
Then, add the matrix to its result vector and then activate gaussian_eliminate_result method from gaussian_elimination_method to get the result vector x.
and then convert the result vector to a polynom.
"""
