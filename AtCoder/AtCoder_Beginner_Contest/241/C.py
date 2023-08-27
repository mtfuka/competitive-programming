N=int(input())
S=[]
for i in range(N):
    S.append(input())

#横
for i in range(N):
    for j in range(N-5):
        count=0
        for k in range(6):
            if S[i][j+k]=='#':
                count+=1
        if count>=4:
            print('Yes')
            exit()
#縦
for i in range(N-5):
    for j in range(N):
        count=0
        for k in range(6):
            if S[i+k][j]=='#':count+=1
        if count>=4:
            print('Yes')
            exit()
#右下がり
for i in range(N-5):
    for j in range(N-5):
        count=0
        for k in range(6):
            if S[i+k][j+k]=='#':count+=1
        if count>=4:
            print('Yes')
            exit()
#右上がり
for i in range(N-5):
    for j in range(5,N):
        count=0
        for k in range(6):
            if S[i+k][j-k]=='#':count+=1
        if count>=4:
            print('Yes')
            exit()
print('No')