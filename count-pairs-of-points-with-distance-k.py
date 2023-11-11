from collections import Counter

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        res = 0
        ctr = Counter()
        for a, b in coordinates:
            for i in range(k + 1):
                res += ctr[(a ^ i, b ^ (k - i))]
            ctr[(a, b)] += 1
        return res