N=int(input())
s=[""]*N
t=[""]*N
for i in range(N):
    s[i],t[i]=input().split()
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and i!=k:
                if (s[i]==s[j] or s[i]==t[j]) and (t[i]==s[k] or t[i]==t[k]):
                    print("No")
                    exit()
print("Yes")
