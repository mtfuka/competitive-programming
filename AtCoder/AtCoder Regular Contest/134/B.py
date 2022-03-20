N=int(input())
s=list(input())
#アルファベットの数をカウント
alphabet_counts=[0 for i in range(26)]
for i in range(N):
    alphabet_counts[ord(s[i])-ord('a')]+=1
#尺取法
tail=N
for i in range(N):
    c=ord(s[i])-ord('a') #先頭文字の数バージョン
    alphabet_counts[c]-=1 #見たので減らす
    exist_alphabet=-1
    #今見ているアルファベットより小さいアルファベットがこの先にあるか
    for j in range(c):
        if alphabet_counts[j]>0:
            exist_alphabet=j
            break
    if exist_alphabet==-1: #なかった場合答えを出力
        continue
    #最小のアルファベットが見つかるまでtailをデクリメント
    while tail>i:
        tail-=1
        t=ord(s[tail])-ord('a') #末尾文字の数バージョン
        alphabet_counts[t]-=1 #見たので減らす
        if t==exist_alphabet:
            s[i],s[tail]=s[tail],s[i]
            break
    if tail<i:
        break
print("".join(s))