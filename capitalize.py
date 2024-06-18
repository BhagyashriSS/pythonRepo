

# Complete the solve function below.
def solve(s):
    lis = list(s.split(" "))
    ans = []
    for i in lis:
        ans.append(i.capitalize())
    return ' '.join(ans)
