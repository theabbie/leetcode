from itertools import permutations
from collections import defaultdict, deque

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        cuboids.sort()
        perms = [[] for _ in range(n)]
        for i in range(n):
            perms[i].extend(list(permutations(cuboids[i])))
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(6):
                        for l in range(6):
                            l1, w1, h1 = perms[i][k]
                            l2, w2, h2 = perms[j][l]
                            if l1 == l2 and w1 == w2 and h1 == h2 and i > j:
                                continue
                            if l1 <= l2 and w1 <= w2 and h1 <= h2:
                                graph[(i, k)].add((j, l))
                                indegree[(j, l)] += 1
        q = deque()
        for i in range(n):
            for j in range(6):
                if indegree[(i, j)] == 0:
                    q.appendleft((i, j))
        order = []
        while len(q) > 0:
            curr = q.pop()
            order.append(curr)
            for i, j in graph[curr]:
                indegree[(i, j)] -= 1
                if indegree[(i, j)] == 0:
                    q.appendleft((i, j))
        order.reverse()
        res = 0
        maxheight = defaultdict(lambda: 0)
        for i, j in order:
            maxheight[(i, j)] = perms[i][j][2]
            for x, y in graph[(i, j)]:
                maxheight[(i, j)] = max(maxheight[(i, j)], perms[i][j][2] + maxheight[(x, y)])
            res = max(res, maxheight[(i, j)])
        return res