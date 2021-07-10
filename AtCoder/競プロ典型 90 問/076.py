N = int(input())
A = list(map(int,input().split()))
a = sum(A)/10
for i in range(N):
    A.append(A[i])
Sum = [A[0]]*(2*N+1)
for i in range(2*N):
    Sum[i+1] = Sum[i]+A[i]
for s in Sum:
    left_index: int = 0
    right_index: int = len(Sum) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = Sum[middle_index]

        if (s+a) < middle_value:
            right_index = middle_index - 1
            continue
        if (s+a) > middle_value:
            left_index = middle_index + 1
            continue
        print("Yes")
        exit()
print("No")