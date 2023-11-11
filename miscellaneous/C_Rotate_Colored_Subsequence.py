n, m = map(int, input().split())

pos = [[] for _ in range(m)]

s = input()

colors = list(map(int, input().split()))

for i in range(n):
    pos[colors[i] - 1].append((i, s[i]))

res = [""] * n

for el in range(m):
    k = len(pos[el])
    for i in range(k):
        res[pos[el][(i + 1) % k][0]] = pos[el][i][1]

print("".join(res))