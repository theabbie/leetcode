import bisect

n, m = map(int, input().split())

b = list(map(int, input().split()))
c = list(map(int, input().split()))

b.sort()

def ctr(x):
    return n - bisect.bisect_left(b, x)

END = max(c) + b[0]

sales = []

for i in range(m):
    res = 0
    beg = 0
    end = END
    while beg <= end:
        mid = (beg + end) // 2
        l, m, r = (mid - 1) * ctr(mid - 1 - c[i]), mid * ctr(mid - c[i]), (mid + 1) * ctr(mid + 1 - c[i])
        if m > l and m > r:
            res = max(res, m)
            break
        if l > m:
            res = max(res, l, m, r)
            end = mid - 1
        else:
            res = max(res, l, m, r)
            beg = mid + 1
    beg = END // 2
    end = END
    while beg <= end:
        mid = (beg + end) // 2
        l, m, r = (mid - 1) * ctr(mid - 1 - c[i]), mid * ctr(mid - c[i]), (mid + 1) * ctr(mid + 1 - c[i])
        if m > l and m > r:
            res = max(res, m)
            break
        if l > m:
            res = max(res, l, m, r)
            end = mid - 1
        else:
            res = max(res, l, m, r)
            beg = mid + 1
    sales.append(res)

print(*sales)