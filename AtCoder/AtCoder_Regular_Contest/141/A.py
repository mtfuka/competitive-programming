import bisect
S=set()
for i in range(1,10):
    for j in range(2,19):
        S.add(int("".join(str(i)*j)))
for i in range(10,100):
    for j in range(3,10):
        S.add(int("".join(str(i)*j)))
for i in range(100,1000):
    for j in range(3,7):
        S.add(int("".join(str(i)*j)))
for i in range(1000,10000):
    for j in range(3,5):
        S.add(int("".join(str(i)*j)))
for i in range(10**4,10**5):
    for j in range(3,4):
        S.add(int("".join(str(i)*j)))
for i in range(10**5,10**6):
    for j in range(3,4):
        S.add(int("".join(str(i)*j)))
# for i in range(10**6,10**7):
#     S.add(str(i)*2)
# for i in range(10**7,10**8):
#     S.add(str(i)*2)
# for i in range(10**8,10**9):
#     S.add(str(i)*2)
# for i in range(10**9,10**10):
#     S.add(str(i)*2)
def shuki2_min(x):
    y=str(x)
    n=len(y)
    if n%2!=0:return 0
    else:
        s1,s2=y[:n//2],y[n//2:]
        if s1<=s2:return int(s1*2)
        else:
            s1=str(int(s1)-1)
            if len(s1)!=len(s2):return 0
            else:return int(s1*2)
l=list(S)
l.sort()
T=int(input())
for i in range(T):
    N=int(input())
    i=max(0,bisect.bisect_right(l,N)-1)
    print(max(l[i],shuki2_min(N)))