from collections import *

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n = len(s)
        ctr = Counter(s)
        ops = max(ctr.values())
        last = {}
        for i in range(n):
            last[s[i]] = i
        return "".join([s[i] for i in range(n) if last[s[i]] == i and ctr[s[i]] == ops])