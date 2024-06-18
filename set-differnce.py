# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(list(map(int,input().split())))
m = int(input())
b = set(list(map(int,input().split())))
dif =a.difference(b)
print(len(dif))
