N=int(input())
H=list(map(int,input().split()))
for i in range(N-1):
    if H[i]<H[i+1]:continue
    else:exit(print(H[i]))
print(H[N-1])