from collections import defaultdict

n, q = map(int, input().split())

parent = defaultdict(lambda: defaultdict(lambda: -1))

arr = list(map(int, input().split()))

for i in range(n - 1):
    parent[i + 2][0] = arr[i]

d = 1
x = 1
while x <= n:
    for el in range(1, n + 1):
        parent[el][d] = parent[parent[el][d - 1]][d - 1]
    d += 1
    x *= 2

for _ in range(q):
    x, k = map(int, input().split())
    curr = x
    p = 0
    while k:
        if k & 1:
            curr = parent[curr][p]
        k //= 2
        p += 1
    print(curr)