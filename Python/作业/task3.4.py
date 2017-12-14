def maxOflist(s,ps,pd):
    if ps >= pd:
        return s[ps]
    mid = (pd + ps) // 2
    return max(maxOflist(s,ps,mid),maxOflist(s,mid + 1,pd))

s = input().split()
s = [int(i) for i in s]
print(maxOflist(s,0,len(s)-1))
