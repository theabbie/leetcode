class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        nxt = [{} for _ in range(n + 1)]
        last = {}
        for i in range(n - 1, -1, -1):
            nxt[i] = dict(last)
            last[s1[i]] = i
        nxt[n] = dict(last)
        res = (0, float('inf'))
        for i in range(n):
            j = i - 1
            for c in s2:
                if c not in nxt[j]:
                    j = float('inf')
                    break
                j = nxt[j][c]
            if j - i + 1 < res[1]:
                res = (i, j - i + 1)
        if res[1] == float('inf'):
            return ""
        return s1[res[0]:res[0]+res[1]]