def greedy(s,k):
    if k == 0:
        return s
    else:
        for i in range(0,len(s)-1):
            if s[i] > s[i + 1]:
                s.pop(i)
                break
        else:
            s.pop()
        return greedy(s,k-1)
while True:
    s = list(input('请输入一个整数:'))
    k = int(input('请输入删去的位数:'))
    print('最小的数是:',''.join(greedy(s,k)),'\n')
