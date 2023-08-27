N = int(input())
A = map(int,input().split())
list = [0] * 200
for Ai in A:
  list[Ai%200] += 1
ans = 0
for value in list:
  ans += value*(value-1)//2
print(ans)
