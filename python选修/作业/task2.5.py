n = 1
s = 0
flag = True
prec = float(input())
while 1/n >= prec:
    if flag:
        s = s + 1/n
        flag = False
    else:
        s = s - 1/n
        flag = True
    n = n + 2
print("%.16f"%(4 * s))
