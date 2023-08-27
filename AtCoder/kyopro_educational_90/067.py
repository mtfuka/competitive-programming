N,K = map(int,input().split())
def f(x):
    x1 = 0
    n1 = 0
    while x>0:
        x1 += x % 10 * (8**n1)
        x //= 10
        n1 += 1
    x2 = 0
    n2 = 0
    while x1>0:
        if (x1 % 9) ==8:
            x2 += 5 * (10**n2)
        else:
            x2 += x1 % 9 * (10**n2)
        x1 //= 9
        n2 += 1
    return x2
for k in range(K):
    N = f(N)
print(N)