t = int(input())

for _ in range(t):
    l, r = input().split()
    if len(l) < len(r):
        l = "0" * (len(r) - len(l)) + l
    n = len(r)
    i = 0
    while i < n and l[i] == r[i]:
        i += 1
    if i < n:
        