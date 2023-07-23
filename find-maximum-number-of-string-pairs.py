from collections import Counter

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        ctr = Counter()
        for w in words:
            res += ctr[w[::-1]]
            ctr[w] += 1
        return res