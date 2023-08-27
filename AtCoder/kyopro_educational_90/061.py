Q = int(input())
l = []
for i in range(Q):
    t,x = map(int,input().split())
    if t==1:
        l.insert(0,x)
    if t==2:
        l.append(x)
    if t==3:
        print(l[x-1])