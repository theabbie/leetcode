from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(set)
        for i in range(n):
            graph[manager[i]].add(i)
        q = deque([(headID, 0)])
        res = 0
        while len(q) > 0:
            curr, t = q.pop()
            res = max(res, t)
            for person in graph[curr]:
                q.appendleft((person, t + informTime[curr]))
        return res