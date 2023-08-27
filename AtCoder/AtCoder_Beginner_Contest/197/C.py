#PyPyでないと通らない
N = int(input())
A = list(map(int, input().split()))
ans = 2**30
for i in range(2**(N-1)): #bit全探索
  OR = A[0]
  XOR = 0
  for j in range(N-1): #シフトする桁数
    if (i>>j)&1: #bit演算
      XOR ^= OR #1だったらそれまでの区間のORをXOR
      OR = A[j+1]
    else:
      OR |= A[j+1] #0だったらOR
  XOR ^= OR #最後の区間のORをXOR
  ans = min(ans,XOR) 
print(ans)
