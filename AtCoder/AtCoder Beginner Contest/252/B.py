N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
food=max(A)
f=[]
for i in range(N):
    if A[i]==food:
        f.append(i+1)
for i in f:
    for j in B:
        if i==j:
            print("Yes")
            exit()
print("No")