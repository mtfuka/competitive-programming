N,A,B=map(int,input().split())
masu=[['' for j in range(B*N)]for i in range(A*N)]
for i in range(A*N):
    for j in range(B*N):
        if i%(2*A)<A and j%(2*B)<B:
            masu[i][j]='.'
        if A<=i%(2*A) and j%(2*B)<B:
            masu[i][j]='#'
        if i%(2*A)<A and B<=j%(2*B):
            masu[i][j]='#'
        if A<=i%(2*A) and B<=j%(2*B):
            masu[i][j]='.'
for i in range(A*N):
    print(''.join(masu[i]))