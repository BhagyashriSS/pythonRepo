#You are given a string and your task is to swap cases. In other words, convert all #lowercase letters to uppercase letters and vice versa.

#For Example:

#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2  



def swap_case(s):
    ans = ""S
    for c in s:
        if(c.isupper() and c.isalpha()):
            ans+=c.lower()
        elif (c.islower() and  c.isalpha()):
            ans+=c.upper()
        else :
            ans+=(c)
    return ans