N = int(input())
A = []
for i in range(2,10000//6+1):
    A.append(6*i)
for i in range(2,10000//10+1):
    A.append(10*i)
for i in range(2,10000//15+1):
    A.append(15*i)
A = list(set(A))
A.insert(0,6)
A.insert(1,10)
A.insert(2,15)
print(*A[:N])