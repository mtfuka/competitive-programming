N,K = map(int,input().split())
MOD = 10**9+7
if N==1:
    print(K)
    exit()
print(K*(K-1)*pow(K-2,N-2,MOD)%MOD)