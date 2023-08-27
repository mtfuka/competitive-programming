N=int(input())
primes = []
is_prime = [True] * (10**6 + 1)
is_prime[0] = False
is_prime[1] = False
for p in range (0, 10**6 + 1):
    if not is_prime[p]:
        continue
    primes.append(p)
    for i in range(p*p, 10**6 + 1, p):
        is_prime[i] = False
ans=0
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if primes[i]*primes[j]**3>N:
            break
        ans+=1
print(ans)