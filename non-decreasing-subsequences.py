from collections import defaultdict

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        graph = defaultdict(set)
        for i in range(n):
            graph[-1].add(i)
            for j in range(i + 1, n):
                if nums[j] >= nums[i]:
                    graph[i].add(j)
        res = set()
        def DFS(graph, i, v, curr):
            if len(curr) >= 2:
                res.add(tuple(curr))
            for j in graph[i]:
                if j not in v:
                    v.add(j)
                    curr.append(nums[j])
                    DFS(graph, j, v, curr)
                    v.remove(j)
                    curr.pop()
        DFS(graph, -1, set(), [])
        return list(res)