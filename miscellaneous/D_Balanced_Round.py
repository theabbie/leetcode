t = int(input())

res = []

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    curr = n
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and arr[i + 1] - arr[i] <= k:
            i += 1
            ctr += 1
        beg = i - ctr + 1
        end = i
        curr = min(curr, beg + n - end - 1)
        i += 1
    res.append(curr)

print(*res)