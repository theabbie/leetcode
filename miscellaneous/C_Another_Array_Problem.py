t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = max(arr) - min(arr)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    for i in range(n + 1):
        p[i] -= x * i
    print(p)