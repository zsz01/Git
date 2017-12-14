a = int(input())
b = int(input())
c = int(input())
if a>b:
    if a>c:
        if b>c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if b>c:
        if a<c:
            print(b,c,a)
        else:
            print(b,a,c)
    else:
        print(c,b,a)
