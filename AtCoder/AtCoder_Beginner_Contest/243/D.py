N,X=map(int,input().split())
S=input()
S_cut=[]
for i in range(N):
    if S[i]=='U' and len(S_cut)>0 and (S_cut[-1]=='L' or S_cut[-1]=='R'):
        S_cut.pop()
    else:
        S_cut.append(S[i])
for i in range(len(S_cut)):
    if S_cut[i]=='U':
        X//=2
    elif S_cut[i]=='L':
        X*=2
    else:
        X=X*2+1
print(X)