n, d = map(int, input().split())

t = sorted(map(int, input().split()))

res = -1

for i in range(1, n):
    if t[i] - t[i - 1] <= d:
        res = t[i]
        break

print(res)