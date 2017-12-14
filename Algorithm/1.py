import time
import random
def partition(arr, pIndex):
	index = 0
	r = len(arr) - 1
	pVal = arr[pIndex]
	arr[pIndex], arr[r] = arr[r], arr[pIndex]
	for i in range(0, r+1):
		if arr[i] < pVal:
			arr[index], arr[i] = arr[i], arr[index]
			index += 1
	arr[index], arr[r] = arr[r], arr[index]
	return index

def getMedian(arr):
	n = len(arr)
	while n > 5:
		cols = n//5
		m = []
		for i in range(0, cols):
			s = sorted(arr[5*i:(5*i+5)])
			m.append(s[2])
		arr = m
		n = len(arr)
	arr.sort()
	return arr[n//2]

def function(arr, k):
	pivot = getMedian(arr)
	pIndex = arr.index(pivot)
	index = partition(arr, pIndex)
	n = len(arr)
	if k < n - index:
		return function(arr[index+1:n], k)
	elif k == n - index:
		return pivot
	elif k > n - index:
		return function(arr[0:index], k-(n-index))

def generate_random():
    n = random.randint(10, 16)
    l = set()
    while n >= 0:
        l.add(random.randint(0, 101))
        n = n - 1
    return l

test = 0
print('测试3组数据:')
while test < 3:
    test += 1
    print('第%d组'%test)
    arr = list(generate_random())
    k1 = time.clock()
    if len(arr) % 2 == 1:
        pivot = function(arr,len(arr)//2)
    else:
        pivot = (function(arr,len(arr)//2) + function(arr,len(arr)//2 - 1))/2
    k2 = time.clock()
    print('原数组:',arr)
    print('中位数:%d,耗时:%fms\n'%(pivot,k2-k1 if len(arr)%2 == 1 else (k2-k1)/2))
