A,B = map(int,input().split())
E = []
for i in range(1,A+1):
  E.append(i*B*(B+1)//2)
for i in range(1,B+1):
  E.append(-i*A*(A+1)//2)
print(*E)