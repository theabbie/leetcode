class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        ctr = [0] * n
        for i in range(n):
            ctr[edges[i]] += i
        return max(range(n), key = lambda i: ctr[i])