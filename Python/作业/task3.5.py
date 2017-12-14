def lcm(a,b):
    add = c = max(a,b)
    while (c % a != 0) or (c % b != 0):
        c += add
    return c

def gcd(a,b):
    i = min(a,b)
    while i >= 1:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

a = input().split('/')
a = [int(i) for i in a]
b = input().split('/')
b = [int(i) for i in b]

fm = lcm(a[1],b[1])
fz = a[0] * (fm // a[1]) + b[0] * (fm // b[1])
print('%d/%d'%(fz/gcd(fz,fm),fm/gcd(fz,fm)))
