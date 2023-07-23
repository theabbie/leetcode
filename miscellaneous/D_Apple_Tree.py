from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    graph = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    q = int(input())
    res = [0] * q
    pos = defaultdict(list)
    stack = [(1, -1)]
    leaves = set()
    lcount = defaultdict(int)
    order = []
    while len(stack) > 0:
        curr, prev = stack.pop()
        order.append((curr, prev))
        for j in graph[curr]:
            if j != prev:
                stack.append((j, curr))
    order.reverse()
    for el, prev in order:
        leaf = True
        for j in graph[el]:
            if j != prev:
                leaf = False
                lcount[el] += lcount[j]
        if leaf:
            lcount[el] += 1
    for i in range(q):
        x, y = map(int, input().split())
        res[i] = lcount[x] * lcount[y]
    print("\n".join(map(str, res)))