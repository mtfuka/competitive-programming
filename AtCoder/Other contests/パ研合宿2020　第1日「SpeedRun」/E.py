X,Y = map(int,input().split())
if X==0 and Y==0:print(1,1)
elif X==0:print(2*Y,Y)
elif Y==0:print(X,2*X)
elif X<Y:print(X+Y,Y)
elif X==Y:print(-1)
elif X>Y:print(X,X+Y)
