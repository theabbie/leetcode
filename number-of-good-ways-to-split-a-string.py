from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        left = Counter()
        lctr = 0
        rctr = len(right)
        res = 0
        for c in s:
            if left[c] == 0:
                lctr += 1
            left[c] += 1
            if right[c] == 1:
                rctr -= 1
            right[c] -= 1
            if lctr == rctr:
                res += 1
        return res