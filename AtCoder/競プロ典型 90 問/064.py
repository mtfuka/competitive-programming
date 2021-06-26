N,Q = map(int,input().split())
A = list(map(int,input().split()))
difference = [0]*(N-1)
for i in range(N-1):
    difference[i] = A[i] - A[i+1]
inconvenience = 0
for i in range(N-1):
    inconvenience += abs(A[i]-A[i+1])
for i in range(Q):
    L,R,V = map(int,input().split())
    if L==1 and R==N:
        print(inconvenience)
    elif L==1:
        inconvenience += abs(difference[R-1]+V) - abs(difference[R-1])
        difference[R-1] += V
        print(inconvenience)
    elif R==N:
        inconvenience += abs(difference[L-2]-V) - abs(difference[L-2])
        difference[L-2] -= V
        print(inconvenience)
    else:
        inconvenience += abs(difference[R-1]+V) - abs(difference[R-1]) + abs(difference[L-2]-V) - abs(difference[L-2])
        print(inconvenience)
        difference[L-2] -= V
        difference[R-1] += V