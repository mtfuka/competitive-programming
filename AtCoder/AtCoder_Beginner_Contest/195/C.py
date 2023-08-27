N = int(input())
ans=0
if 10**3<=N:ans+=N-10**3+1
if 10**6<=N:ans+=N-10**6+1
if 10**9<=N:ans+=N-10**9+1
if 10**12<=N:ans+=N-10**12+1
if N==10**15:ans+=1
print(ans)
