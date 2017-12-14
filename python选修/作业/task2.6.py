import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            break
    else:
        return True
    return False

n = int(input())
L = []
for i in range(2,n+1):
    if isPrime(i):
        L.append(i)
for i in range(0,len(L)-1):
    print(L[i],end = ' ')
print(L[len(L)-1])
