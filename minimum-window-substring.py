from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ctrTarget = Counter(t)
        i = 0
        j = 0
        ctr = Counter()
        ms = (0, float('inf'))
        while i <= j:
            valid = True
            for c in ctrTarget:
                if ctr[c] < ctrTarget[c]:
                    valid = False
                    break
            if valid:
                if (j - i) <= ms[1] - ms[0]:
                    ms = (i, j)
                ctr[s[i]] -= 1
                i += 1
            else:
                if j >= n:
                    break
                ctr[s[j]] += 1
                j += 1
        if ms[1] == float('inf'):
            return ""
        return s[ms[0]:ms[1]]