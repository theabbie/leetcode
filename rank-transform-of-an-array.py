import heapq

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        dist = sorted(set(arr))
        for i, d in enumerate(dist):
            ranks[d] = i + 1
        return [ranks[item] for item in arr]