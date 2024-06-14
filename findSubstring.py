def count_substring(string, sub_string):
    pos = 0
    count = 0
    while pos< len(string):
        pos = string.find(sub_string, pos)
        if  pos != -1:
            pos += 1
            count +=1
        else:
           break
    return count