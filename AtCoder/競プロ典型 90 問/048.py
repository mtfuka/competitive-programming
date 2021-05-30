N,K = map(int,input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())
C = [0]*2*N
for i in range(N):
    C.append(A[i]-B[i])
    C.append(B[i])
C.sort()
print(sum(C[-K:]))