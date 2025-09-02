from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        tctr = Counter()
        for c in t:
            tctr[c] += 1
        ctr = Counter()
        def check(curr):
            for c in tctr:
                if tctr[c] > ctr[c] - int(curr == c):
                    return False
            return True
        reslength = -1
        res = ""
        i = 0
        for j in range(n):
            ctr[s[j]] += 1
            while i < j and check(s[i]):
                ctr[s[i]] -= 1
                i += 1
            if check(-1):
                if reslength == -1 or j - i + 1 < reslength:
                    reslength = j - i + 1
                    res = s[i:j+1]
        return res