t = int(input())

def squaresum(n):
    return n * (n + 1) * (2 * n + 1) // 6

def squaresumrange(l, r):
    l = max(l - 1, 0)
    return squaresum(r) - squaresum(l)

ranges = []

ctr = 0
for i in range(1, 2024):
    ranges.append((ctr + 1, ctr + i))
    ctr += i

for _ in range(t):
    n = int(input())
    i = 0
    while i < len(ranges) and not ranges[i][0] <= n <= ranges[i][1]:
        i += 1
    res = 0
    l = r = n
    loff = n - ranges[i][0]
    roff = ranges[i][1] - n
    for j in range(i, -1, -1):
        res += squaresumrange(ranges[j][0] + loff, ranges[j][1] - roff)
        loff -= 1
        roff -= 1
        loff = max(loff, 0)
        roff = max(roff, 0)
    print(res)