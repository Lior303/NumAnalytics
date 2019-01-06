def get_L(lst_x, i, x):
    reduce = 1
    for k in range(0, len(lst_x)):
        if(k!=i):
            reduce *= ((x - lst_x[k][0]) / float(lst_x[i][0] - lst_x[k][0]))
    return reduce

def get_P(x, lst_y):
    sum=0
    for i in range(0,len(lst_y)):
        sum+=(get_L(table_points, i, x)*lst_y[i][1])
        print("Current sum: {}".format(sum))
    return sum

def get_Polynomial(table_points):
    return lambda x:get_P(x, table_points)

table_points =[]
# table_points = [ (8.1, 16.9446), (8.3, 17.56492), (8.6, 18.50515), (8.7, 18.82091) ]
print("Enter number of table points=")
n=int(input())
for i in range(n):
    print("Enter table points:")
    point = (float(input("x=")), float(input("y=")))
    table_points.append(point)
poly = get_Polynomial(table_points)
print("Enter the value of X0: ")
x0 = float(input(""))
print("\nThe value of the polynomial at point x is: {}".format(poly(x0)))