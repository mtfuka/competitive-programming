import decimal
import math
X,Y,R=map(decimal.Decimal,input().split())
ans=0
for i in range(math.ceil(X-R),math.floor(X+R)+1):
    top=math.floor(Y+(R**2-(i-X)**2).sqrt())
    bottom=math.ceil(Y-(R**2-(i-X)**2).sqrt())
    ans+=top-bottom+1
print(ans)