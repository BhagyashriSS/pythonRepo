#You are given a 2-D array with dimensions N X M.
#Your task is to perform the min function over axis 1 and then find the max of that.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n,m = list(map(int,input().split()))
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

matrix = np.array(matrix)
mins = np.min(matrix,axis=1)
print(np.max(mins))
    
