N,H,X=map(int,input().split())
P=list(map(int,input().split()))
for i,p in enumerate(P):
    if H+p>=X:
        print(i+1)
        exit()
