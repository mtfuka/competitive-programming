#PyPyでないと通らない
N = int(input())
A,B,C = list(map(int, input().split()))
ans = float("INFINITY")
for i in range(9999):
  for j in range(9999-i):
    if N-A*i-B*j>=0 and (N-A*i-B*j)%C==0:
      ans = min(ans,i+j+(N-A*i-B*j)//C)
print(ans)