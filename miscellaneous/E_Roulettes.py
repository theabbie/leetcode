n, m = map(int, input().split())

res = 0

vals = []

total = 0

for _ in range(n):
    vals.append(list(map(int, input().split())))
    total += vals[-1][0]

for curr in vals:
    curramount = 0
    for el in curr[2:]:
        curramount += curr[0] * m / el
    curramount //= curr[1]
    res += curramount * curr[0] / total

print(res)