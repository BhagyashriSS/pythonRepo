# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(list(map(int,input().split())))
m = int(input())
b = set(list(map(int,input().split())))
uni =a.intersection(b)
print(len(a)+len(b)-len(uni))
