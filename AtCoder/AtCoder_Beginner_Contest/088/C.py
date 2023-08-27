c = [list(map(int,input().split())) for i in range(3)]
bool = False
if c[0][0]-c[0][1]==c[1][0]-c[1][1]==c[2][0]-c[2][1]:
	if c[0][1]-c[0][2]==c[1][1]-c[1][2]==c[2][1]-c[2][2]:
		if c[0][0]-c[1][0]==c[0][1]-c[1][1]==c[0][2]-c[1][2]:
			if c[1][0]-c[2][0]==c[1][1]-c[2][1]==c[1][2]-c[2][2]:bool=True

if(bool):print("Yes")
else:print("No")
