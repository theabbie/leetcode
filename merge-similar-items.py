from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = defaultdict(int)
        for v, w in items1:
            weights[v] += w
        for v, w in items2:
            weights[v] += w
        res = []
        for v in sorted(weights.keys()):
            res.append([v, weights[v]])
        return res