import math
X,A,D,N=map(int,input().split())
if (D>=0 and X<=A) or (D<0 and X>=A):print(abs(X-A))
elif (D>=0 and A+D*(N-1)<=X) or (D<0 and A+D*(N-1)>=X):print(abs(X-A-D*(N-1)))
else:
    n1=math.floor((X-A)/D+1)
    n2=math.ceil((X-A)/D+1)
    print(min(abs(X-A-D*(n1-1)),(abs(X-A-D*(n2-1)))))