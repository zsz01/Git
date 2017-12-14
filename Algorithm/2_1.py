while True:
    n = int(input('请输入物体数目:'))
    m = int(input('请输入背包容量:'))
    w = input('请输入%d个物体质量:'%n).split()
    v = input('请输入%d个物体价值:'%n).split()
    w.insert(0,'0')
    v.insert(0,'0')
    s = [[ 0 for i in range(m+1) ] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if j < int(w[i]):
                s[i][j] = s[i-1][j]
            else:
                s[i][j] = max(s[i-1][j],s[i-1][j-int(w[i])]+int(v[i]))
    result = [0 for i in range(n)]
    for i in range(n,0,-1):
        if s[i][m] > s[i-1][m]:
            result[i-1] = 1
            m -= int(w[i])
    print('选择方案是:',result,'\n最大价值为:',s[n][-1],'\n')
