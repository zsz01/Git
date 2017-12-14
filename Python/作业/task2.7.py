def function(n):
    if (n % 5 == 1) and ((n - 1) // 5 != 0):
        return True
    else:
        return False
    
def recover(n):
    return (n - 1) // 5 * 4

n = 1
while True:
    cnt = 0
    temp = n
    flag = True
    while cnt < 5:
        cnt += 1
        if function(temp):
            temp = recover(temp)
        else:
            flag = False;
    if flag:
        break
    else:
        n += 1
print('一共捕了%d条鱼'%(n))
