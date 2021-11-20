K = int(input())
divisors = []
i = 1
while i*i<=K:
    if K%i==0:
        divisors.append(i)
        if i!=K//i:
            divisors.append(K//i)
    i += 1
ans = 0
for i in range(len(divisors)):
    for j in range(i,len(divisors)):
        a=divisors[i]
        b=divisors[j]
        c=K//(a*b)
        if a>b:
            continue
        if K%(a*b)!=0:
            continue
        if b<=c:
            ans += 1
print(ans)