ABC=list(map(int,input().split()))
ABC.sort()
if ABC[0]+ABC[1]-ABC[2]>=0:
    print(ABC[2])
else:
    print(-1)