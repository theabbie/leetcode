m, n, d = map(int, input().split())

res = -1

a = list(map(int, input().split()))

b = list(map(int, input().split()))

a.sort()
b.sort()

i = 0

for el in b:
    while i < m and a[i] < el - d:
        i += 1
    if i < m and el - d <= a[i] <= el + d:
        res = max(res, el + a[i])

i = 0

for el in b:
    while i < m and a[i] <= el + d:
        i += 1
    if i > 0 and el - d <= a[i - 1] <= el + d:
        res = max(res, el + a[i - 1])

print(res)