def function(l,cnt,n):
    if cnt == n-1:
        for i in range(0,n):
            print(l[i],end = '')
        print()
        return
    for i in range(cnt,n):
        l[cnt],l[i] = l[i],l[cnt]
        function(l,cnt+1,n)
        l[cnt],l[i] = l[i],l[cnt]

n = int(input())
l = [i for i in range(1,n+1)]
function(l,0,n)
