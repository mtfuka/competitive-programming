A,B,C,D=map(int,input().split())
prime=[True]*201
prime[0]=False
prime[1]=False
for i in range(2,16):
    for j in range(i*i,201,i):
        prime[j]=False
for i in range(A,B+1):
    flag=True
    for j in range(C,D+1):
        flag&=not prime[i+j]
    if flag==True:
        print('Takahashi')
        exit()
print('Aoki')