n = int(input('请输入n:'))
m = int(input('请输入m:'))
t = input('请输入%d个作业时间:'%n).split()
t = [int(i) for i in t]
res = float('Inf')
machine = list(0 for i in range(m))
def backtrack(cnt):
    global res
    if(cnt == n):
        if res > max(machine):
            res = max(machine)
        return
    for i in range(m):
        machine[i] += t[cnt]
        backtrack(cnt + 1)
        machine[i] -= t[cnt]
if n <= m:
    print('最早完成时间为:%d\n'%max(t))
else:
    backtrack(0)
    print('最早完成时间为:%d\n'%res)
