import numpy as np

def jacobi(A,b,N=25,x=None):
    if x is None:
        x = np.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        x = (b - np.dot(R,x)) / D
        print("The guess in this iteration: {}".format(x))
    return x

A = np.array([[2.0,1.0],[5.0,7.0]])
b = np.array([11.0,13.0])
guess = np.array([1.0,1.0])

sol = jacobi(A,b,N=25,x=guess)

print("\nThe result vector X: {}".format(sol))