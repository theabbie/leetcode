t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(k):
        if arr[i] > k:
            res += 1
    print(res)