t = int(input())

pres = []

def check(r, p):
    res = 0
    while p % r == 0:
        p //= r
        res += 1
    return p == 1 and res > 2

for _ in range(t):
    n = int(input())
    if n <= 3:
        pres.append("NO")
        continue
    res = "NO"
    for p in range(3, 11):
        beg = 2
        end = 10 ** 9
        bres = beg
        while beg <= end:
            mid = (beg + end) // 2
            if (pow(mid, p) - 1) // (mid - 1) <= n:
                bres = mid
                beg = mid + 1
            else:
                end = mid - 1
        if sum(bres ** i for i in range(p)) == n:
            res = "YES"
            break
    if res == "YES":
        pres.append(res)
        continue
    for r in range(2, 51):
        if check(r, n * (r - 1) + 1):
            res = "YES"
            break
    pres.append(res)

print("\n".join(pres))