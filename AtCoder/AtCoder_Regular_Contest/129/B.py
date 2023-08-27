from math import inf
N=int(input())
maxL,minR=0,inf
for i in range(N):
  L,R=map(int,input().split())
  if L>maxL:maxL=L
  if R<minR:minR=R
  if maxL<minR:print(0) #共通範囲がある場合は0
  else:print((maxL-minR+1)//2) #ない場合は中点との距離