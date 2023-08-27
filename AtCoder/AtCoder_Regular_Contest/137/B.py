N=int(input())
A=list(map(int,input().split()))
S=[0 for i in range(N+1)]
Score_Max,Score_min,S_Max,S_min=0,0,0,0
for i in range(N):
    if A[i]==0:
        S[i+1]=S[i]+1
    else:
        S[i+1]=S[i]-1
    S_Max=max(S_Max,S[i+1])
    S_min=min(S_min,S[i+1])
    Score_Max=max(Score_Max,S[i+1]-S_min)
    Score_min=min(Score_min,S[i+1]-S_Max)
print(Score_Max-Score_min+1)