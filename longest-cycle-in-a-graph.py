class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        res = -1
        v = set()
        for node in range(n):
            i = 0
            pos = {}
            while node != -1 and node not in v:
                pos[node] = i
                v.add(node)
                node = edges[node]
                i += 1
            if node != -1 and node in pos:
                res = max(res, i - pos[node])
        return res