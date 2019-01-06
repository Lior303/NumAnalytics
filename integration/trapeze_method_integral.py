def trapeze_method(a, b, f, n=50):
    h=(b-a)/float(n)
    result=h
    sum=0
    Xi =[]
    for i in range(n+1):
        Xi.append(a+i*h)
    for i in range(n+1):
        print("The current sum is: {}".format(sum))
        if(i==0 or i==n):
            sum+=0.5*(f(Xi[i]))
        else:
            sum+=f(Xi[i])
    print("The result equal to result (1/3*h) * sum {}".format(sum))
    result*=sum
    print("\nThe area below the function f(x) is: {}".format(result))
    return abs(result)

print("Enter a function f(x): ")
func=eval("lambda x: " + input(""))
print("Enter range: a and b")
a,b=float(input("a=")), float(input("b="))
trapeze_method(a, b, func)
