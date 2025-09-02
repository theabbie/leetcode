from collections import Counter

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = Counter()
        for a, b in pairs:
            graph[a].append(b)
            degree[b] -= 1
            degree[a] += 1
        res = []
        def solve(i):
            while graph[i]:
                solve(graph[i].pop())
            res.append(i)
        solve(min(degree, key = lambda x: 0 if degree[x] == 1 else 1))
        res.reverse()
        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]