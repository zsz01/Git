def factor(n):
    res = 1
    if n <= 1:
        return res
    while n >= 2:
        res *= n
        n -= 1
    return res
n = int(input())
print(factor(n))
