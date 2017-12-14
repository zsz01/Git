s = input().split()
s = [int(i) for i in s]
ans = []
for i in s:
    if i not in ans:
        ans.append(i)
for i in range(len(ans)-1):
    print(ans[i],end = ' ')
print(ans[-1])
