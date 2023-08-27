N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
food=max(A)
for i in range(K):
    if A[B[i]-1]==food:
            print("Yes")
            exit()
print("No")