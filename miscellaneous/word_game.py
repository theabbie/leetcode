t = int(input())

for _ in range(t):
    n = int(input())
    a = set(input().split())
    b = set(input().split())
    c = set(input().split())
    sa = sb = sc = 0
    for w in set.intersection(a, b):
        if w not in c:
            sa += 1
            sb += 1
    for w in set.intersection(b, c):
        if w not in a:
            sb += 1
            sc += 1
    for w in set.intersection(c, a):
        if w not in b:
            sc += 1
            sa += 1
    for w in set.difference(a, set.union(b, c)):
        sa += 3
    for w in set.difference(b, set.union(a, c)):
        sb += 3
    for w in set.difference(c, set.union(a, b)):
        sc += 3
    print(sa, sb, sc)