def P_ij(x, i, j, table_points):
    if(i==j):
        #return yi
        return table_points[i][1]
    temp = (x-table_points[j][0])*P_ij(x, i, j-1, table_points) - (x-table_points[i][0])*P_ij(x, i+1, j, table_points)
    temp= temp/float(table_points[i][0] - table_points[j][0])
    print("P" + str(i)+ str(j) + " = " + str(temp))
    return temp

def get_Neville(table_points):
    n=len(table_points)-1
    return lambda x: P_ij(x, 0, n, table_points)

table_points =[]
print("Enter number of table points=")
n=int(input())
for i in range(n):
    print("Enter table points:")
    point = (float(input("x=")), float(input("y=")))
    table_points.append(point)
poly = get_Neville(table_points)
print("Enter the value of X0: ")
x0 = float(input(""))
print("The value of the polynomial at point x is: {}".format(poly(x0)))