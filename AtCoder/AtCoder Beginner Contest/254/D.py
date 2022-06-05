def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
N=int(input())
l=[]
d={}
for i in range(1,N+1):
    d[i*i]=1
ans=0
for i in range(1,N+1):
    if i in d:
        for j in d:
            if j<=N:
                ans+=1
            else:
                break
    else:
        f=factorization(i)
        cnt=1
        for j in range(len(f)):
            if f[j][1]%2==1:
                cnt*=f[j][0]
        for j in d:
            if cnt*j<=N:
                ans+=1
            else:
                break
print(ans)