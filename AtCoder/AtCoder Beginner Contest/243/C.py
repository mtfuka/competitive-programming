N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    X[i],Y[i]=map(int,input().split())
S=input()
left_max,right_min={},{}
for i in range(N):
    if S[i]=='L':
        if Y[i] in left_max:
            left_max[Y[i]]=max(X[i],left_max[Y[i]])
        else:
            left_max[Y[i]]=X[i]
    else:
        if Y[i] in right_min:
            right_min[Y[i]]=min(X[i],right_min[Y[i]])
        else:
            right_min[Y[i]]=X[i]
for i in range(N):
    if Y[i] in right_min and Y[i] in left_max:
        if right_min[Y[i]]<left_max[Y[i]]:
            print("Yes")
            exit()
print("No")