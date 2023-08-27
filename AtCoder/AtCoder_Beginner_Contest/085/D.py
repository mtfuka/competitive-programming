N, H = map(int, input().split())
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
b=sorted(b,reverse=True) #攻撃力高い順に投げるので降順ソートする
ans=0
maxa=max(a)
for i in range(N):
    if b[i]>maxa:
      H-=b[i]
      ans+=1
      if(H<=0):
        print(ans)
        exit()
ans+=(H+maxa-1)//maxa
print(ans)
