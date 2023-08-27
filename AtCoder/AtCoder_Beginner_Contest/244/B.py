N=int(input())
T=input()
x,y=0,0
d=['e','s','w','n']
i=0
for ti in T:
    if ti=='S':
        if d[i]=='e':
            x+=1
        elif d[i]=='s':
            y-=1
        elif d[i]=='w':
            x-=1
        elif d[i]=='n':
            y+=1
    if ti=='R':
        i=(i+1)%4
print(x,y)