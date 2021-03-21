N = int(input())
S = [0]
for _ in range(N):
    S.append(input())

def f(x):#再帰関数
  if x==1 and S[1]=='AND':return 1
  if x==1 and S[1]=='OR':return 3

  if S[x]=='AND':return f(x-1) #数学的考察をするとこのような漸化式で表せる
  if S[x]=='OR':return 2**x+f(x-1) #ORでxN=Trueの時は残り全部True,Falseの2通りどちらでも良いので+2^N

print(f(N))
