S = input()
ans = ''
for i in range(1,len(S)+1):
  if S[-i]=='9':
    ans += '6'
  elif S[-i]=='6':
    ans += '9'
  else:
    ans += S[-i]
print(ans)