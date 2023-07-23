t = int(input())

def check(segs, q, mid, n):
    arr = [0] * n
    for i in range(mid):
        arr[q[i]] = 1
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    for l, r in segs:
        if 2 * (p[r + 1] - p[l]) > r - l + 1:
            return True
    return False

for _ in range(t):
    n, m = map(int, input().split())
    segs = []
    for _ in range(m):
        l, r = map(int, input().split())
        segs.append((l - 1, r - 1))
    q = int(input())
    pos = []
    for _ in range(q):
        i = int(input())
        pos.append(i - 1)
    beg = 0
    end = q
    res = -1
    while beg <= end:
        mid = (beg + end) // 2
        if check(segs, pos, mid, n):
            res = mid
            end = mid - 1
        else:
            beg = mid + 1
    print(res)