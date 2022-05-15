N=int(input())
S=list(input())
ARC=0
l=[]
for i in range(N-2):
    if S[i]=='A' and S[i+1]=='R' and S[i+2]=='C':
        ARC+=1
        j=1
        while i-j>=0 and i+2+j<N and S[i-j]=='A' and S[i+2+j]=='C':
            j+=1
        l.append(j)
print(min(sum(l),2*len(l)))