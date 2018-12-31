def trapeze_method(a, b, f, n):
    h=(b-a)/float(n)
    result=h
    sum=0
    Xi =[]
    for i in range(n+1):
        Xi.append(a+i*h)
    for i in range(n+1):
        if(i==0 or i==n):
            sum+=0.5*(f(Xi[i]))
        else:
            sum+=f(Xi[i])
    result*=sum
    print("The area below the function f(x) is: {}".format(result))
    return abs(result)

print("Enter a function f(x): ")
func=eval("lambda x: " + input(""))
print("Enter range: a and b")
a,b=float(input("a=")), float(input("b="))
print("Enter number of equals sections: ")
n=int(input("n="))
trapeze_method(a, b, func, n)
