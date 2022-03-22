N=int(input())
l=list(range(1,2*N+2))
ans=[]
for i in range(N+1):
    print(l.pop(0))
    if i==N:
        exit()
    aoki=int(input())
    l.remove(aoki)