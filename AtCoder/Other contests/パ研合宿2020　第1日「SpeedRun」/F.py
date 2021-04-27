#PyPyでないと通らない
P = int(input())
fib = [1,1]
for i in range(P*P):
    fib.append((fib[i]+fib[i+1])%P)
for i in range(P*P):
    if fib[i]%P==0:
        print(i+1)
        exit()
print(-1)