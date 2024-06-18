#You are given a 2-D array with dimensions N cross M.
#Your task is to perform the  sum tool over axis 0  and then find the prouduct of that #result.

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy
if __name__ == "__main__":
    n,m = map(int, input().split())
    matrix = []
    for i in range(n):
        a = []
        string = list(map(int,input().split()))
        for j in string:
            a.append(j)
        matrix.append(a)
    matrix = numpy.array(matrix)
    sumArray = numpy.sum(matrix,axis = 0)
    prod = 1
    print(numpy.prod(sumArray))
