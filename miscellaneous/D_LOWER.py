n = int(input())

s = list(input())

q = int(input())

res = [[-1, s[i]] for i in range(n)]

lower = upper = -1

for _ in range(q):
    t, x, c = input().split()
    t, x = int(t), int(x) - 1
    if t == 1:
        res[x][0] = _
        res[x][1] = c
    elif t == 2:
        lower = _
    else:
        upper = _

for i in range(n):
    if max(lower, upper) > res[i][0]:
        if lower > upper:
            res[i][1] = res[i][1].lower()
        else:
            res[i][1] = res[i][1].upper()

print("".join(res[i][1] for i in range(n)))