t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pb = [0] * (n + 1)
    for i in range(n):
        pb[i + 1] += pb[i] + b[i]
    diff = [0] * (n + 1)
    extra = [0] * n
    for i in range(n):
        beg = 0
        end = n - 1
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if pb[mid + 1] - pb[i] <= a[i]:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        if res != -1:
            diff[i] += 1
            diff[res + 1] -= 1
        if res < n - 1:
            extra[res + 1] += a[i] - (pb[res + 1] - pb[i])
    res = [0] * n
    for i in range(1, n + 1):
        diff[i] += diff[i - 1]
    for i in range(n):
        res[i] += diff[i] * b[i] + extra[i]
    print(*res)