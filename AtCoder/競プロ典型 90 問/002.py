N = int(input())
def judge(a):
  left_right = 0
  for i in range(len(a)):
    if a[i]=='(': left_right += 1
    if a[i]==')': left_right -= 1
    if left_right < 0: return False
  if left_right == 0: return True
  else: return False 
for i in range(2**N):
  String = ''
  for j in range(N):
    if ((i>>(N-1-j))&1)==0:
      String += '('
    else:
      String += ')' 
  if judge(String):
    print(String)