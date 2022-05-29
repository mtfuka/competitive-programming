import math
N,A,B=map(int,input().split())
sum=(N+1)*N//2
a_sum=(A+N//A*A)*(N//A)//2
b_sum=(B+N//B*B)*(N//B)//2
gcd=A*B//math.gcd(A,B)
ab_sum=(gcd+N//gcd*gcd)*(N//gcd)//2
print(sum-a_sum-b_sum+ab_sum)