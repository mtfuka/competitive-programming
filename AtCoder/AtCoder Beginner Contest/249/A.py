A,B,C,D,E,F,X=map(int,input().split())
Takahashi,Aoki=0,0
for i in range(1,X+1):
    if 1<=i%(A+C)<=A:
        Takahashi+=B
    if 1<=i%(D+F)<=D:
        Aoki+=E
if Takahashi>Aoki:
    print("Takahashi")
elif Takahashi<Aoki:
    print("Aoki")
else:
    print("Draw")    