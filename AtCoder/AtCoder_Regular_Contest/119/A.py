N = int(input())
b = 0
while True:
  if 2**b <= N < 2**(b+1):
    break
  b += 1
ans = N
for i in range(1,b+1):
  ans = min(ans,N//(2**i)+i+N%(2**i))
print(ans)