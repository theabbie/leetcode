from collections import *

class Solution:
    def minimumPushes(self, word: str) -> int:
        pos = [1] * 8
        ctr = Counter(word)
        res = 0
        for c in sorted(ctr, key = lambda x: -ctr[x]):
            i = min(range(8), key = lambda x: pos[x])
            res += ctr[c] * pos[i]
            pos[i] += 1
        return res