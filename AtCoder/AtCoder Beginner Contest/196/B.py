N = str(input())
for i in range(len(N)):
  if N[i]=='.':
    print(N[:i])
    exit()
print(N)
