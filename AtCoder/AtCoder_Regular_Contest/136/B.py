N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a=sorted(A)
b=sorted(B)
if a==b:
  if len(A)>len(set(A)):
    print('Yes')
    exit()
  countA=0
  countB=0
  for i in range(N):
    for j in range(i+1,N):
      if A[i]>A[j]:
        countA+=1
      if B[i]>B[j]:
        countB+=1
  if (countA-countB)%2==0:
    print('Yes')
  else:
    print('No')
else:
  print('No')