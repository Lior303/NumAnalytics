import numpy as np
from  matrix.gaussian_elimination_method import gaussian_eliminate_result_adapter as gauss_elim
from matrix.matrix_iteration import Matrix, addKwargs

def polynomial_approximation(data, matrixSolver = gauss_elim):
    """
    :param data: the dictionary that was given
    :return: result vector as a polynom.
    """
    def createMatrix():
        """
        create the matrix
        :return: the matrix from the dictionary
        """
        size = len(data.keys())
        return np.matrix([[x ** i for i in range(size - 1, -1, -1)] for x in data.keys()])

    def createResultsVector():
        """
        :return: the resut vector
        """
        return np.matrix([[y] for y in data.values()])

#     def unpackVector(vector):
#         return vector.flatten()

    matrixA , vectorB = createMatrix(), createResultsVector()
    vectorX = matrixSolver(matrixA,vectorB)
    if isinstance(vectorX, np.matrix):
        vectorX = vectorX.flatten().tolist()[0]
        print(vectorX)
    return np.poly1d(vectorX)

if __name__ == '__main__':
    print("Enter a table of points of table and values of table.\nAs dictionary {<key1>:<val1>, ..., <keyn>:<valn>}:")
#     data = eval(input())
#     polynomial_approximation(data)
#     print(polynomial_approximation({1:1, 10:0.1, 20:0.05}))
    solver = addKwargs(Matrix.iterGaussSeidel,n=10)
    print(polynomial_approximation({1:1, 10:0.1, 20:0.05},matrixSolver=solver))


"""
polynomial approximation. calculate and return the polynom from the polynomial approximation of a known dictionary (the table)
first, crate the matrix using the ductionary, then create resut vector ---> it will be the values of the dictionary.
Then, add the matrix to its result vector and then activate gaussian_eliminate_result method from gaussian_elimination_method to get the result vector x.
and then convert the result vector to a polynom.
"""
