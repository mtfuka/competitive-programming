x1,y1,x2,y2=map(int,input().split())
def dist_sq(a,b,c,d):
    return (a-c)**2+(b-d)**2
for i in range(x1-2,x1+3):
    for j in range(y1-2,y1+3):
        if dist_sq(x1,y1,i,j)==dist_sq(x2,y2,i,j)==5:
            print("Yes")
            exit()
print("No")