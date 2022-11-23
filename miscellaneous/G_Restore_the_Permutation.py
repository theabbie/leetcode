t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    used = set(arr)
    if 2 * len(set(arr)) < n:
        print(-1)
        continue
    res = [None] * n
    for i in range(n):
        if i % 2 == 1:
            res[i] = arr[i // 2]
    pos = True
    for i in range(n // 2 - 1, -1, -1):
        curr = arr[i] - 1
        while curr >= 1 and curr in used:
            curr -= 1
        if curr >= 1:
            res[2 * i] = curr
            used.add(curr)
        else:
            pos = False
    if pos:
        print(*res)
    else:
        print(-1)