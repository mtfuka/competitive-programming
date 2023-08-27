n = int(input())
x = 0
left: int = 1
right: int = n+1
while left<=right:
  middle: int = (left+right)//2
  if middle**2+middle-2*n-2<=0 and (middle+1)**2+middle+1-2*n-2>0:
    break
  elif middle**2+middle-2*n-2<0:
    left = middle + 1
  elif middle**2+middle-2*n-2>0:
    right = middle - 1
print(n+1-middle)