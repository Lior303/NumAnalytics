import numpy as np
import matrix_functions as func

def pivot_row(A, k):
    i_max = k
    for i in range(k + 1, len(A)):
        if abs(A[i][k]) > abs(A[i - 1][k]):
            i_max = i
    return i_max

def forward_eliminate(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n)):
        func.pprint(A)
        i_max = pivot_row(A, k)
        if A[i_max][k] == 0:
            break
        A[k], A[i_max] = A[i_max], A[k]  # Operation 1: swap
        for i in range(k + 1, m):
            c = A[i][k] / A[k][k]  # Operation 3: linear
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - c * A[k][j]
            A[i][k] = 0.0

def backward_substitute(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n) - 1, 0, -1):  # [min(m, n), 1]
        func.pprint(A)
        if A[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):  # [k - 1, 0]
            c = A[i][k] / A[k][k]
            for j in range(i, n):
                A[i][j] = A[i][j] - c * A[k][j]  # Operation 3: linear
    for i in range(min(m, n)):
        func.pprint(A)
        if A[i][i] == 0:
            continue
        for j in range(n - 1, i - 1, -1):  # [n - 1, i]
            A[i][j] = A[i][j] / A[i][i]  # Operaton 2: scale

def gaussian_eliminate(A):
    A=A.tolist()
    for i in range(len(A)-1):
        if(len(A[i])!=len(A[i+1])):
            exit("The matrix rows need to be at the same length")
    forward_eliminate(A)
    backward_substitute(A)
    return A

def gaussian_eliminate_result(A):
    if(func.cond_calc(A)<1):
        print("The cond of matrix A is less then 1")
        return
    print("Cond of matrix A: {}\n".format(func.cond_calc(A)))
    A=gaussian_eliminate(A)
    print("Final matrix A:\n")
    func.pprint(A)
    lst=[x[len(A)] for x in A]
    print("Vector x (result): {}".format(lst))
    return lst

def gaussian_eliminate_result_adapter(A,b):
    return gaussian_eliminate_result(np.append(A,b, axis=1))


def demo():
    A = np.matrix("1 2 3 4; 4 5 6 7; 7 8 9 3")
    gaussian_eliminate_result(A)

if __name__ == "__main__":
    demo()