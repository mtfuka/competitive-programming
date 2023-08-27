h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0
for A11 in range(1,h1+1):
    for A12 in range(1,h1-A11+1):
        for A21 in range(1,h2+1):
            for A22 in range(1,h2-A21+1):
                A13=h1-A11-A12
                A23=h2-A21-A22
                A31=w1-A11-A21
                A32=w2-A12-A22
                if A13<=0 or A23<=0 or A31<=0 or A32<=0:
                    continue
                if h3-A31-A32==w3-A13-A23 and h3-A31-A32>0:
                    ans+=1
print(ans)