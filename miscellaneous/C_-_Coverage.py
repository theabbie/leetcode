n, m = map(int, input().split())

sets = []

check = set(range(1, n + 1))

for _ in range(m):
    l = int(input())
    sets.append(set(map(int, input().split())))

res = 0

for mask in range(1 << m):
    curr = set()
    for i in range(m):
        if mask & (1 << i):
            curr.update(sets[i])
    if check.issubset(curr):
        res += 1

print(res)