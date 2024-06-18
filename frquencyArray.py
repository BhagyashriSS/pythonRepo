from collections import Counter
n = input(int())
rooms = list(map(int,input().split()))
frq = Counter(rooms)
print(frq)
for key,val in frq.items():
    if(val == 1):
        print(int(key))
        break
