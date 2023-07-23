from collections import deque, defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        q = deque()
        indegree = [0] * n
        graph = defaultdict(set)
        revgraph = defaultdict(set)
        for a, b in relations:
            indegree[b - 1] += 1
            graph[a - 1].add(b - 1)
            revgraph[b - 1].add(a - 1)
        for i in range(n):
            if indegree[i] == 0:
                q.appendleft(i)
        res = [0] * n
        while len(q) > 0:
            curr = q.pop()
            res[curr] = time[curr]
            for j in revgraph[curr]:
                res[curr] = max(res[curr], time[curr] + res[j])
            for j in graph[curr]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.appendleft(j)
        return max(res)