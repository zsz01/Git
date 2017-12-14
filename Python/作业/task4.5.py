s = input()
a = ord('a')
lst = [chr(i) for i in range(a,a+26)]
ans = [0 for i in range(26)]
for i in s:
    if i != ' ':
        ans[ord(i) - a] += 1

for i in range(26):
    if ans[i] != 0:
        print(lst[i],ans[i])
