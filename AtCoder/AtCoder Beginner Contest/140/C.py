N = int(input())
B = list(map(int,input().split()))
ans = B[0]+B[N-2] #初項と末項は先に足しておく
for i in range(N-2):
    ans += min(B[i],B[i+1])
print(ans)