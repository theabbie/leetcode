from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ctr = Counter()
        for el in words:
            ctr["".join(sorted(set(el)))] += 1
        res = 0
        for el in ctr:
            res += ctr[el] * (ctr[el] - 1) // 2
        return res