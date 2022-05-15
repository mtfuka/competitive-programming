W=int(input())
print(297)
A=[]
for i in range(1,100):
    A.append(i)
    A.append(i*100)
    A.append(i*10000)
print(*A)