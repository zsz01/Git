lst = []
for i in range(5):
    a = int(input())
    lst.append(a)
for i in lst:
    print('%2d'%i,end = '')
    for j in range(i):
        print('#',end = '')
    print()
