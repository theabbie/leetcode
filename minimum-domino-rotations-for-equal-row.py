class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        res = float('inf')
        for a in range(1, 7):
            cost = 0
            for i in range(n):
                if tops[i] == a:
                    continue
                if bottoms[i] == a:
                    cost += 1
                else:
                    cost = float('inf')
            res = min(res, cost)
        for a in range(1, 7):
            cost = 0
            for i in range(n):
                if bottoms[i] == a:
                    continue
                if tops[i] == a:
                    cost += 1
                else:
                    cost = float('inf')
            res = min(res, cost)
        if res == float('inf'):
            res = -1
        return res