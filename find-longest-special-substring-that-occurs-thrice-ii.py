from collections import *

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        lens = defaultdict(list)
        i = 0
        res = -1
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            lens[s[i]].append(ctr)
            if ctr >= 3:
                res = max(res, ctr - 2)
            i += 1
        for c in lens:
            curr = sorted(lens[c])
            if len(curr) >= 3:
                res = max(res, curr[-3])
            if len(curr) >= 2:
                if curr[-1] > curr[-2]:
                    res = max(res, curr[-2])
                elif curr[-2] >= 2:
                    res = max(res, curr[-2] - 1)
        return res