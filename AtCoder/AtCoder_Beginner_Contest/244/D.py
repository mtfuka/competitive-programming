S1,S2,S3=input().split()
T1,T2,T3=input().split()
match=0
if S1==T1:match+=1
if S2==T2:match+=1
if S3==T3:match+=1
if match==1:
    print("No")
else:
    print("Yes")