n, m = map(int, input().split())

arr = set()

if m > 0:
    arr = set(map(int, input().split()))

res = []

seen = set()

for i in range(1, n + 1):
    if i not in seen:
        curr = set()
        j = i
        while j in arr:
            curr.add(j)
            curr.add(j + 1)
            j += 1
        seen.update(curr)
        if len(curr) == 0:
            res.append(i)
        else:
            res.extend(sorted(curr, reverse = True))

print(*res)