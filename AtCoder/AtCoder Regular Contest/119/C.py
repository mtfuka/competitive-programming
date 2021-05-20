N = int(input())
A = list(map(int,input().split()))

sumA = [0]
for i in range(N):
    if i%2==0:
        sumA.append(sumA[i]+A[i])
    if i%2==1:
        sumA.append(sumA[i]-A[i])

count = {}
for a in sumA:
    count[a] = count.get(a,0) + 1

ans = 0
for c in count:
    ans += count[c]*(count[c]-1)//2
print(ans)