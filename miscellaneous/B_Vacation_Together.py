m, n = map(int, input().split())

days = [0] * n

for _ in range(m):
    s = input()
    for i in range(n):
        if s[i] == "x":
            days[i] = 1

res = 0

i = 0

while i < n:
    ctr = 1
    while i < n - 1 and days[i] == days[i + 1]:
        i += 1
        ctr += 1
    if days[i] == 0:
        res = max(res, ctr)
    i += 1

print(res)