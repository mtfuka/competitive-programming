N,Q=map(int,input().split())
S=input()
X=0
for i in range(Q):
    t,x=map(int,input().split())
    if t==1:
        X+=x
    else:
        print(S[(x-1-X)%N])