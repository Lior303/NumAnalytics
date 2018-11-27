from math import log

def optimal_iteration(a, b, epsilon):
    """
    calcuate the optimal number of iterations until the result will converge
    :param a: point a
    :param b: point b
    :param epsilon: fault degree allowed
    :return: the optimal number of iterations
    """
    div=epsilon/float(b-a)
    return abs(round(-1*log(div,2)-1))

def bisection_method(aX, bX, f, epsilon=10**-4):
    """
    bisection method. to calculate x's (roots) of a function
    :param aX: point a
    :param bX: point b
    :param f: the function
    :param epsilon: fault degree allowed
    """
    if(f(aX)*f(bX)>0):
        print("Error! f(a) and f(b) don't have opposite signs")
        return
    num_iteration = optimal_iteration(aX, bX, epsilon)
    count = 0
    mX = (aX + bX) / 2.0
    while(count<num_iteration and abs(f(mX))>epsilon):
        print("aX: {}, bX: {}".format(aX, bX))
        if(f(aX)*f(mX)<0):
            bX=mX
        else:
            aX=mX
        count+=1
        mX = (aX + bX) / 2.0
    print("\nThe root is: " + str(mX))

print("Enter a function f(x): ")
func=eval("lambda x: " + input(""))
print("Enter range: a and b")
bisection_method(float(input("a=")), float(input("b=")), func)

"""
bisection method limitations:
1) if a and b are very close (small numbers) then, b-a will be zero and then its a division by zero.
2) bisection method can only work if f(a)*f(b)>0.
3) bisection method wont work for every function ---> the optimal number may not converge
"""