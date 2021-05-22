import math
def combinations_count(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
A,B,K = (map(int,input().split()))
ans = ''
for i in range(A+B-1):
  if B==0:
    ans+='a'*A
    break
  elif A==1 and B==1 and K==1:
    ans+='ab'
    break
  elif A==1 and B==1 and K==2:
    ans+='ba'
    break
  elif A==0:
    ans+='b'*B
    break
  elif K<=combinations_count(A+B-1, B):
    ans += 'a'
    A -= 1
  else:
    ans += 'b'
    K -= combinations_count(A+B-1, B)
    B -= 1
print(ans)
