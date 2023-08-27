import numpy as np
K,N,M = map(int,input().split())
A = np.array(input().split(),np.int64)

B = M*A//N
C = N*B-M*A
n = M - sum(B)

#n番目に小さい値までの全てのインデックスを取得
ids = np.argpartition(C,n-1)[:n]
B[ids] += 1
print(*B)