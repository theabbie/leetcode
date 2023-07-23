t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    lake = []
    for _ in range(m):
        lake.append(list(map(int, input().split())))
    v = set()
    res = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in v and lake[i][j] > 0:
                stack = [(i, j)]
                currv = {(i, j)}
                while len(stack) > 0:
                    p, q = stack.pop()
                    for x, y in [(p - 1, q), (p, q - 1), (p + 1, q), (p, q + 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in currv and lake[x][y] > 0:
                            currv.add((x, y))
                            stack.append((x, y))
                curr = 0
                for x, y in currv:
                    curr += lake[x][y]
                res = max(res, curr)
                v.update(currv)
    print(res)