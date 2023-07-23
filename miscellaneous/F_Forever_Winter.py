from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    indegree = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        indegree[a] += 1
        indegree[b] += 1
    ctr = Counter(indegree)
    res = (-1, -1)
    for x in range(2, n + 1):
        if (n - x - 1) % x == 0:
            y = (n - x - 1) // x
            ideal = Counter()
            ideal[x] += 1
            ideal[y + 1] += x
            ideal[1] += x * y
            if ctr == ideal:
                res = (x, y)
                break
    print(*res)