def get_A(lst):
    if(len(lst)==1):
        # y value
        return lst[0][1]
    return (get_A(lst[1::])-get_A(lst[:len(lst)-1]))/float(lst[len(lst)-1][0] - lst[0][0])

def get_F(index, lst):
    return get_A(lst[:index+1])

def get_var(index, table_points, x):
    mult=get_F(index, table_points)
    for i in range(index):
        mult*=(x-table_points[i][0])
    return mult

def get_Poly(x, table_points):
    n=len(table_points)
    sum=0
    for i in range(n):
        sum+=get_var(i, table_points, x)
        print("Current sum: {}".format(sum))
    return sum

def get_Newton_Polynomial(table_points):
    return lambda x: get_Poly(x, table_points)

table_points =[]
# table_points = [ (8.1, 16.9446), (8.3, 17.56492), (8.6, 18.50515), (8.7, 18.82091) ]
print("Enter number of table points=")
n=int(input())
for i in range(n):
    print("Enter table points:")
    point = (float(input("x=")), float(input("y=")))
    table_points.append(point)
poly = get_Newton_Polynomial(table_points)
print("Enter the value of X0: ")
x0 = float(input(""))
print("The value of the polynomial at point x is: {}".format(poly(x0)))