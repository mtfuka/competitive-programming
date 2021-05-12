#Pythonでないと通らない
N = int(input())
T = input()

P,Q,R = '','',''
string = False
for i in range(N):
    if i%3==0:
        P += '1'
        Q += '1'
        R += '0'
    if i%3==1:
        P += '1'
        Q += '0'
        R += '1'
    if i%3==2:
        P += '0'
        Q += '1'
        R += '1'
if T==P or T==Q or T==R:
    string = True

if string:
    if T=='1':
        print(10**10*2)
        exit()
    elif T=='11':
        print(10**10)
        exit()
    else:
        n = T.count('0')
        if T[-1]=='1':
            print(10**10-n)
            exit()
        elif T[-1]=='0':
            print(10**10+1-n)
            exit()
else:
    print(0)