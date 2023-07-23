n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

for i in range(m):
    res += a[b[i] - 1]

print(res)