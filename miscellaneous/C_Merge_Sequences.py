m, n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = sorted(a + b)

pos = {}

for i in range(m + n):
    pos[res[i]] = i + 1

print(*[pos[el] for el in a])
print(*[pos[el] for el in b])