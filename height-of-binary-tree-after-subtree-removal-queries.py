from sortedcontainers import SortedList
from collections import *

class Solution:
    def treeQueries(self, root, queries):
        levels = defaultdict(SortedList)
        level = {}
        height = {}
        def dfs(r, l):
            if not r:
                return 0
            level[r.val] = l
            a = dfs(r.left, l + 1)
            b = dfs(r.right, l + 1)
            res = 1 + max(a, b)
            height[r.val] = res
            levels[l].add(res)
            return res
        dfs(root, 0)
        res = []
        for node in queries:
            l = level[node]
            h = height[node]
            levels[l].remove(h)
            res.append(l + (levels[l] or [0])[-1] - 1)
            levels[l].add(h)
        return res