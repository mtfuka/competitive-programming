N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for Bi in B:
    if Bi in A:
        A.remove(Bi)
    else:
        print('No')
        exit()
print('Yes')