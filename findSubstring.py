#In this challenge, the user enters a string and a substring.
#You have to print the number of times that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left.


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
