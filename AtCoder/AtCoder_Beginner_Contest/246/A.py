x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
if x1==x2:
    x=x3
if x3==x2:
    x=x1
if x1==x3:
    x=x2
if y1==y2:
    y=y3
if y3==y2:
    y=y1
if y1==y3:
    y=y2
print(x,y)