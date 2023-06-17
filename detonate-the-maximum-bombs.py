from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        graph = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if i != j and (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    graph[i].add(j)
        res = 0
        for i in range(n):
            v = {i}
            stack = [i]
            while len(stack) > 0:
                curr = stack.pop()
                for j in graph[curr]:
                    if j not in v:
                        v.add(j)
                        stack.append(j)
            res = max(res, len(v))
        return res