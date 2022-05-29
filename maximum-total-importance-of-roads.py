from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        roadctr = defaultdict(int)
        for a, b in roads:
            roadctr[a] += 1
            roadctr[b] += 1
        total = 0
        bigcities = sorted(range(n), key = lambda c: roadctr[c])
        for i in range(n):
            total += (i + 1) * roadctr[bigcities[i]]
        return total