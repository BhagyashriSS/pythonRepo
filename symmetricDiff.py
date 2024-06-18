# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(list(map(int,input().split())))
n = int(input())
b = set(list(map(int,input().split())))
c = (a.difference(b))
d = b.difference(a)
e = sorted(c.union(d))
for i in e:
    print(i)
