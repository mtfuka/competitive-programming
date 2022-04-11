S=list(input())
S[3]=S[2]
S[2]=S[1]
S[1]=S[0]
S[0]='0'
print("".join(S))