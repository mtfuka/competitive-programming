a,b,x,y = map(int, input().split())
if a>b+1:print(min(2*x,y)*(a-b-1)+x)
if a==b+1 or a==b:print(x)
if a<b:print(min(2*x,y)*(b-a)+x)