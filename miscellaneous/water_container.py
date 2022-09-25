from collections import defaultdict, deque

t = int(input())

for tt in range(1, t + 1):
    n, q = map(int, input().split())
    parent = defaultdict(list)
    child = {}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        parent[min(u, v)].append(max(u, v))
        child[max(u, v)] = min(u, v)
    total = defaultdict(int)
    for _ in range(q):
        curr = int(input())
        while curr in child:
            curr = child[curr]
        total[curr] += 1
    res = 0
    for qq in list(total.keys()):
        q = deque([(qq, 0)])
        ctr = defaultdict(int)
        while len(q) > 0:
            curr, l = q.pop()
            ctr[l] += 1
            for j in parent[curr]:
                q.appendleft((j, l + 1))
        for l in sorted(ctr.keys()):
            if total[qq] >= ctr[l]:
                res += ctr[l]
                total[qq] -= ctr[l]
    print(f"Case #{tt}: {res}")