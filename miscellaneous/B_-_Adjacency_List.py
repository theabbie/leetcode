n, m = map(int, input().split())

l = [set() for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)

for c in range(1, n + 1):
    print(len(l[c]), *sorted(l[c]))