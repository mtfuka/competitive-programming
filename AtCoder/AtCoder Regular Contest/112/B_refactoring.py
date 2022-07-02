B,C=map(int,input().split())
a,b,c,d=B-C//2,B+(C-2)//2,-B-(C-1)//2,-B+(C-1)//2
if C==1:b=B
print(2+b-a+d-c-max(0,min(b,d)-max(a,c)+1))