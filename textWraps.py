

def wrap(string, max_width):
    unit = ''
    ans = ''
    for c in string:
        unit+=c
        if len(unit)==4:
            ans = ans + unit + '\n'
            unit = ''
    if(len(unit)>0):
        ans = ans + unit + '\n'
    return ans
        
        


