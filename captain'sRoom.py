from collections  import Counter
input()
a=list(map(int,input().split()))
x=Counter(a)
for key in x.keys():
    if x[key]==1:
        print(key)
