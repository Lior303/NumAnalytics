def simpson_method(f, a, b, n=50):
    """
    the function calculate integral of f(x) from a to b by the trapezoid rule.
    The trapezoid rule approximates the integral of f(x) from a to b by the sum:
    (h/3)*(f(a) + 2f(a+h) + 4f(a+2h) + 2f(a+3h) + 4f(a+4h) + ... + f(b))
    h = (b - a)/N.
    :param f: function to calculate integral
    :param a: minimum edge of range
    :param b: maximum edge of range
    :param N: number to divide range into
    :return: integral of f(x) from a to b
    """

    h=(b-a)/float(n)
    result = 1/3 * h
    sum = f(a) + f(b)
    Xi = []
    for i in range(n + 1):
        Xi.append(a + i * h)
    for i in range(1, n):
        print("The current sum is: {}".format(sum))
        if(i%2==1):
            sum += 4*f(Xi[i])
        else:
            sum += 2*(f(Xi[i]))
    print("The result equal to result (1/3*h) * sum {}".format(sum))
    result *= sum
    print("\nThe area below the function f(x) is: {}".format(abs(result)))
    return abs(result)

print("Enter a function f(x): ")
func=eval("lambda x: " + input(""))
print("Enter range: a and b")
a,b=float(input("a=")), float(input("b="))
simpson_method(func, a, b)