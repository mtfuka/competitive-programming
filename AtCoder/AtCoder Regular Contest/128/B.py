T=int(input())
for i in range(T):
    ball=list(map(int,input().split()))
    ball.sort()
    if (ball[1]-ball[0])%3==0:
        print(ball[1])
    elif (ball[2]-ball[0])%3==0:
        print(ball[2])
    elif (ball[2]-ball[1])%3==0:
        print(ball[2])
    else:
        print(-1)