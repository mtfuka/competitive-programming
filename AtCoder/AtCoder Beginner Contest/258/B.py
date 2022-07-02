N=int(input())
A=[]
for i in range(N):
    A.append(input())
ans=0
for i in range(N):
    for j in range(N):
        a,b,c,d,e,f,g,h="","","","","","","",""
        for k in range(N):
            a+=A[(i+k)%N][j]
            b+=A[(i-k)%N][j]
            c+=A[i][(j+k)%N]
            d+=A[i][(j-k)%N]
            e+=A[(i+k)%N][(j+k)%N]
            f+=A[(i+k)%N][(j-k)%N]
            g+=A[(i-k)%N][(j+k)%N]
            h+=A[(i-k)%N][(j-k)%N]
        ans=max(ans,int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h))
print(ans)