import bisect
x=list(input())
X=int("".join(x))
l=[]
for fir in range(1,10):
    for d in range(-9,9):
        s=[]
        num=fir
        for dg in range(18):
            s.append(str(num))
            l.append(int("".join(s)))
            num+=d
            if not 0<=num<=9:break
l.sort()
i=bisect.bisect_left(l,X)
print(l[i])