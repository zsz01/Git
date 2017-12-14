n = int(input('请输入物体数目:'))
c = int(input('请输入背包容量:'))
w = input('请输入%d个物体质量:'%n).split()
v = input('请输入%d个物体价值:'%n).split()
w = [int(i) for i in w]
v = [int(i) for i in v]

jmplist = [(0,0)]
tmp = [(0,0)]

def isOk(t,w):
    return t+w <= c

def fx(w):
    return w[0]

def check(tmp,jmplist):
    removelist = set()
    for i in tmp:
        if i not in jmplist:
            jmplist.append(i)
    cnt = len(jmplist)
    i = 0
    j = 0
    jmplist.sort(key = fx)
    while i < cnt:
        while j < cnt:
            if jmplist[i][0] >= jmplist[j][0] and jmplist[i][1] <= jmplist[j][1] and i != j:
                del jmplist[i]
                i = 0
                j = 0
                cnt = cnt - 1
                jmplist.sort(key = fx)
                break
            else:
                j += 1
        i += 1
        j = 0

for i in range(n-1,-1,-1):
    for j in range(0,len(jmplist)):
        if isOk(jmplist[j][0],w[i]):
            tmp.append((jmplist[j][0]+w[i],jmplist[j][1]+v[i]))
    check(tmp,jmplist)
    tmp = [i for i in jmplist]
ans = -1
for i in jmplist:
    if ans < i[1]:
        ans = i[1]
print('跳跃表为:',jmplist)
print('最大价值为:',ans)
