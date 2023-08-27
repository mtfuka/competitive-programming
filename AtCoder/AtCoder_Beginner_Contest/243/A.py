V,A,B,C=map(int,input().split())
for i in range(1000000):
    if i%3==0:
        V-=A
        if V<0:
            print('F')
            exit()
    if i%3==1:
        V-=B
        if V<0:
            print('M')
            exit()
    if i%3==2:
        V-=C
        if V<0:
            print('T')
            exit()
                        