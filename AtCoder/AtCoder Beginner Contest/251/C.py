N=int(input())
S=[]
T=[]
for i in range(N):
    Si,Ti=input().split()
    S.append(Si)
    T.append(int(Ti))
original={}
ans=[]
for i in range(N):
    if not S[i] in original:
        original[S[i]]=T[i]
        ans.append([S[i],T[i],i])
highest=-1
index=0
for i in range(len(ans)):
    if highest<ans[i][1]:
        highest=ans[i][1]
        index=ans[i][2]+1
print(index)