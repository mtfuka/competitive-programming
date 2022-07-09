L,R=map(int,input().split())
S=list(input())
for i in range((R-L+1)//2):
    S[L-1+i],S[R-1-i]=S[R-1-i],S[L-1+i]
print("".join(S))