N,M = map(int,input().split())
A = list(map(int,input().split()))
import heapq
A = [-1*a for a in A] #ヒープの最大値を取り出すために-1倍
heapq.heapify(A)
for i in range(M):
    max = heapq.heappop(A)*(-1) #最大値(=最小値*(-1))を取得
    heapq.heappush(A,max//2*(-1)) #半額にして戻す
print(sum(A)*(-1))
