s = input().split()
s = [int(i) for i in s]
maxData = s[0]
for i in range(len(s)):
    if s[i] > maxData:
        maxData = s[i]

for i in range(len(s)):
    print(i+1,s[i],end = ' ')
    if s[i] >= maxData - 10:
        print('A')
    elif s[i] >= maxData - 20:
        print('B')
    elif s[i] >= maxData - 30:
        print('C')
    elif s[i] >= maxData - 40:
        print('D')
    else:
        print('F')
    
