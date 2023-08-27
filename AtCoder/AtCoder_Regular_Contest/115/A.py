N, M = map(int, input().split())
count1_odd = 0
for _ in range(N):
  S = input()
  if S.count('1')%2==1: #1の数が奇数個の場合
    count1_odd +=1 #奇数個だけ数えれば残りは偶数個
print(count1_odd*(N-count1_odd)) #奇数個と偶数個の積
