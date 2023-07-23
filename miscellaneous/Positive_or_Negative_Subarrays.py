t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    p = 0
    q = 0
    for i in range(n):
        if arr[i] == 1:
            p += i + 1
        else:
            q += i + 1
    print(abs(p - q))