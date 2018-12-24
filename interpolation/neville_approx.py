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

# table_points = [(0,1), (0.05, 0.951229), (0.15, 0.860708), (0.25, 0.778801)
table_points = [(0,5), (1,2), (2,-5), (3,-10)]

poly = get_Neville(table_points)
print(poly(3))