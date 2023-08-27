H,W,X,Y = map(int, input().split())
S = [input() for _ in range(H)]

#center
ans = 1

#down
for i in range(H-X):
  if S[X+i][Y-1]=='.': ans += 1
  else:break

#right
for i in range(W-Y):
  if S[X-1][Y+i]=='.': ans += 1
  else:break

#up
for i in range(X-1):
  if S[X-2-i][Y-1]=='.': ans += 1
  else:break

#left
for i in range(Y-1):
  if S[X-1][Y-2-i]=='.': ans += 1
  else:break

print(ans)
