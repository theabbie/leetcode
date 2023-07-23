t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = -1
    savings = 0
    for i in range(n):
        savings += 5000 - arr[i]
        if savings >= k:
            res = i + 1
            break
    print(res)