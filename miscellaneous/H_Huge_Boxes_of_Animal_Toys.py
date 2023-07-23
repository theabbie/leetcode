t = int(input())

for _ in range(t):
    res = ["Ya", "Ya", "Ya", "Ya"]
    a, b, c, d = map(int, input().split())
    if a == b:
        res[0] = res[1] = "Tidak"
    if a == 0 and d == 0:
        res[0] = res[3] = "Tidak"
    if b == 0 and c == 0:
        res[1] = res[2] = "Tidak"
    sign = 1
    if a > 0:
        sign *= 1 if a % 2 == 0 else -1
    if b > 0:
        sign *= 1 if b % 2 == 0 else -1
    if sign == 1:
        res[0] = res[1] = "Tidak"
    else:
        res[2] = res[3] = "Tidak"
    print(*res)