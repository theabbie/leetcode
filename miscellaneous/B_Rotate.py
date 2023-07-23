n = int(input())

b = []

for _ in range(n):
    b.append(list(input()))

pos = []

for i in range(n - 1):
    pos.append((0, i))

for i in range(n - 1):
    pos.append((i, n - 1))

for i in range(n - 1):
    pos.append((n - 1, n - i - 1))

for i in range(n - 1):
    pos.append((n - i - 1, 0))

beg = b[pos[-1][0]][pos[-1][1]]

for i in range(len(pos) - 1, 0, -1):
    b[pos[i][0]][pos[i][1]] = b[pos[i - 1][0]][pos[i - 1][1]]

b[pos[0][0]][pos[0][1]] = beg

print("\n".join("".join(r) for r in b))