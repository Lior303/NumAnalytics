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
    return sum

def get_Polynomial(table_points):
    return lambda x:get_P(x, table_points)

table_points = [(0,1), (1,0), (2,1)]
poly = get_Polynomial(table_points)
print(poly(3))