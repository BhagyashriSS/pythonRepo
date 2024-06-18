# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m = list(map(int,input().split()))
matrix = []
for i in range (n):
    row = list(map(int,input().split()))
    matrix.append(row)
matrix = np.array(matrix)

print(np.mean(matrix,axis = 1))
print(np.var(matrix,axis = 0))
print(round(np.std(matrix,axis =None),11))
