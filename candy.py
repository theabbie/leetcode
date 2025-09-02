class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                graph[i].append(i + 1)
                indeg[i + 1] += 1
            if ratings[i] > ratings[i + 1]:
                graph[i + 1].append(i)
                indeg[i] += 1
        res = [0] * n
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                res[i] = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    res[v] = res[u] + 1
                    q.append(v)
        return sum(res)