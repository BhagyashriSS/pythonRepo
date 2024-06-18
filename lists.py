
if __name__ == '__main__':
    N = int(input())
    preview = []
    for _ in range(N):
        case = list(input().split())
        if (case[0] == "insert"):
            preview.insert(int(case[1]), int(case[2]))
        elif case[0] == "remove":
            preview.remove(int(case[1]))
        elif case[0] == "append":
            preview.append(int(case[1]))
        elif case[0] == "sort":
            preview.sort()
        elif case[0] == "pop":
            preview.pop()
        elif case[0] == "reverse":
            preview.reverse()
        elif case[0] == "print":
            print(preview)
        else:
            continue


            
