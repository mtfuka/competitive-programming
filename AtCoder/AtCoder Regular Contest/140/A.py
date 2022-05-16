from collections import Counter
N,K=map(int,input().split())
S=input()
for i in range(1,N//2+1):
    if N%i!=0:continue
    ans=0
    for j in range(i):
        m=max(Counter(S[j::i]).values()) #i個飛ばしで文字の種類数が多いものに合わせる
        ans+=N//i-m #繰り返し数-mが変更したい文字数
    if ans<=K:exit(print(i))
#f(N)=N,どんな繰り返し構造にもできなかったものが残っているのでNを出力
print(N)