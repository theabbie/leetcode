from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        ctr = Counter()
        for el in hours:
            res += ctr[(24 - (el % 24)) % 24]
            ctr[el % 24] += 1
        return res