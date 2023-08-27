import bisect
N = int(input())
a = [0]*2*N
c = ['0']*2*N
for i in range(2*N):
    a[i],c[i] = input().split()
a = list(map(int,a))
if c.count('R')%2==0 and c.count('G')%2==0 and c.count('B')%2==0:
    print(0)
else:
    r = []
    g = []
    b = []
    for i in range(2*N):
        if c[i]=='R':r.append(a[i])
        if c[i]=='G':g.append(a[i])
        if c[i]=='B':b.append(a[i])
    r.sort()
    g.sort()
    b.sort()
    rg,gb,br = float("inf"),float("inf"),float("inf")
    for gi in g:
        if len(b)!=0:
            index = bisect.bisect_left(b,gi)
            if index==0:
                gb = min(gb,abs(b[index]-gi))
            elif index==len(b):
                gb = min(gb,abs(b[index-1]-gi))
            else:
                gb = min(gb,abs(b[index-1]-gi),abs(b[index]-gi))
    for ri in r:
        if len(b)!=0:
            index = bisect.bisect_left(b,ri)
            if index==0:
                br = min(br,abs(b[index]-ri))
            elif index==len(b):
                br = min(br,abs(b[index-1]-ri))
            else:
                br = min(br,abs(b[index-1]-ri),abs(b[index]-ri))
    for gi in g:
        if len(r)!=0:
            index = bisect.bisect_left(r,gi)
            if index==0:
                rg = min(rg,abs(r[index]-gi))  
            elif index==len(r):
                rg = min(rg,abs(r[index-1]-gi))           
            else:
                rg = min(rg,abs(r[index-1]-gi),abs(r[index]-gi))
    if c.count('R')%2==0:
        print(min(gb,br+rg))
    if c.count('G')%2==0:
        print(min(br,gb+rg))
    if c.count('B')%2==0:
        print(min(rg,br+gb))