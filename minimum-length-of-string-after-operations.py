from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        ctr = Counter(s)
        for c in ctr:
            x = ctr[c]
            while x >= 3:
                x -= 2
            res += x
        return res