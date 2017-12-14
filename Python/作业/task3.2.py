n = int(input())

def f(n):
    n1 = n2 = 1
    if n <= 2:
        return n1
    while(n > 2):
        n1,n2 = n2,n2+n1
        n -= 1
    return n2

print(f(n))
