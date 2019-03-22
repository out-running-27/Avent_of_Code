import ast
import numpy as np

f = open('input.txt', 'r')
x = f.readlines()
f.close()

zeors_array=[]
for i in range(len(x)):
    x[i] = x[i].replace('#', '[')
    x[i] = x[i].replace('@', '], [')
    x[i] = x[i].replace(':', '] , [')
    x[i] = x[i].replace('x', ',')
    x[i] = x[i] + ']'
    x[i] = ast.literal_eval(x[i])  
 
for i in range(len(x)):
    zeors_array.append(np.zeros( (1000, 1000) )) 
    zeors_array[i][x[i][1][1]:(x[i][1][1] + x[i][2][1]), x[i][1][0]:(x[i][1][0] + x[i][2][0])] = np.ones((x[i][2][1],x[i][2][0]), dtype=np.int32 )
big_sum_matrix=sum(zeors_array)
elements = big_sum_matrix[ np.where( big_sum_matrix > 1 ) ]
print(len(elements)) #number of squares that are doubled up
