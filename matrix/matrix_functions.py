def pprint(A):
    """
    print he matrix --->works only for list of lists
    :param A: list of lists
    """
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

def inverse(A):
    return A.getI()

def norm_calc(A):
    """
    calculate the norm of a matrix A
    :param A: the matrix
    :return: norm of A
    """
    B=A.tolist()
    lst=[]
    for i in range(len(B)):
        lst.append(sum(B[i]))
    return max(lst)

def cond_calc(A):
    """
    calculate the cond of matrix A
    :param A: the matrix
    :return: the cond of A
    """
    return norm_calc(A)*norm_calc(inverse(A))