m, n = map(int, input().split())

res = 0

for _ in range(m):
    res += input().count("#")

print(res)