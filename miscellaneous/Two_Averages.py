t = int(input())

def minops(a, b, m, n):
    res = float('inf')
    p = k * n - b
    q = a - m
    r = k - 1
    s = b * m - a * n
    for x in range(6 * m + 6 * n + 1):
        beg = 0
        end = 10 ** 12
        while beg <= end:
            mid = (beg + end) // 2
            if p * x + q * mid + r * x * mid > s:
                res = min(res, x + mid)
                end = mid - 1
            else:
                beg = mid + 1
    if res == float('inf'):
        return -1
    return res

for _ in range(t):
    m, n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sum(a)
    b = sum(b)
    print(minops(a, b, m, n))