x1,y1,x2,y2=map(int,input().split())
move=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
for move1 in move:
    for move2 in move:
        if x1+move1[0]+move2[0]==x2 and y1+move1[1]+move2[1]==y2:
            print("Yes")
            exit()
print("No")