A,B,C,D=map(int,input().split())
prime=[True]*201
prime[0]=False
prime[1]=False
for i in range(15):
    if prime[i]:
        for j in range(i*i,201,i):
            prime[j]=False
for i in range(A,B+1):
    if all(not prime[i+j] for j in range(C,D+1)):
        print('Takahashi')
        exit()
print('Aoki')