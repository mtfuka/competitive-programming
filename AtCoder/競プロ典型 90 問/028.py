N=int(input())
a=[[0 for i in range(1001)]for j in range(1001)]
#二次元いもす法
for i in range(N):
    lx,ly,rx,ry=map(int,input().split())
    #重みの加算、角を＋1or-1
    a[lx][ly]+=1
    a[rx][ry]+=1
    a[lx][ry]-=1
    a[rx][ly]-=1
for i in range(1000):
    for j in range(1001):
       #横方向への累積和
       a[i+1][j]+=a[i][j]
for i in range(1001):
    for j in range(1000):
       #縦方向への累積和
       a[i][j+1]+=a[i][j]
#aはマス(i,j)に何枚重なっているかを持つ
ans=[0 for i in range(N+1)]
for i in range(1001):
    for j in range(1001):
       if a[i][j]>0:ans[a[i][j]]+=1
for i in range(1,N+1):
    print(ans[i])