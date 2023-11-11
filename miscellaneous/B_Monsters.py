import math
import bisect

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    order = sorted(arr)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + order[i]
    time = [0] * n
    for i in range(n):
        x = math.ceil(max(arr[i] - k, 0) / k)
        rem = arr[i] - x * k
        j = bisect.bisect_left(order, rem)
        time[i] += p[n] - p[j] - rem * (n - j)
    print(*sorted(range(1, n + 1), key = lambda p: (time[p - 1], p)))