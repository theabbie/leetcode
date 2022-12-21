t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = b = c = 0
    for i in range(n):
        if arr[i] != i + 1:
            a += 1
        if arr[i] != n - i:
            b += 1
    if n % 2 == 0:
        if arr[n // 2 - 1] != n // 2:
            c += 1
        if arr[n // 2] != 1 + n // 2:
            c += 1
    else:
        if arr[n // 2] != 1 + n // 2:
            c += 1
    a -= c
    b -= c
    if a < b and a % 2 == 1:
        print("First")
    elif b < a and b % 2 == 1:
        print("Second")
    else:
        print("Tie")