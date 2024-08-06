from collections import deque

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        q = deque([0])
        graph = [[] for _ in range(n)]
        for i in range(n):
            if parents[i] != -1:
                graph[parents[i]].append(i)
        order = []
        while q:
            curr = q.pop()
            order.append(curr)
            for j in graph[curr]:
                q.appendleft(j)
        order.reverse()
        vals = [set() for _ in range(n)]
        res = [0] * n
        for i in order:
            vals[i].add(nums[i])
            MEX = 1
            for j in graph[i]:
                MEX = max(MEX, res[j])
                if len(vals[i]) < len(vals[j]):
                    vals[i], vals[j] = vals[j], vals[i]
                vals[i].update(vals[j])
                vals[j] = set()
            while MEX in vals[i]:
                MEX += 1
            res[i] = MEX
        return res