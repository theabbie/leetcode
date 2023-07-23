t = int(input())

for _ in range(t):
    m = int(input())
    res = [-1] * m
    parts = []
    for __ in range(m):
        n = int(input())
        parts.append(set(map(int, input().split())))
    curr = set()
    for i in range(m - 1, -1, -1):
        for j in parts[i]:
            if j not in curr:
                res[i] = j
                break
        if len(curr) < len(parts[i]):
            curr, parts[i] = parts[i], curr
        for j in parts[i]:
            curr.add(j)
    if min(res) == -1:
        print(-1)
    else:
        print(*res)