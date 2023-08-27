N=int(input())
A=list(map(int,input().split()))
ball=[]
cnt=0
for i in range(N):
    cnt+=1
    if len(ball)==0 or ball[-1][0]!=A[i]:
        ball.append([A[i],1])
    else:
        ball[-1][1]+=1
        if ball[-1][1]==A[i]:
            cnt-=A[i]
            ball.pop(-1)
    print(cnt)