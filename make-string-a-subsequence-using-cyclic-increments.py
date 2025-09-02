class Solution:
    def canMakeSubsequence(self, a: str, b: str) -> bool:
        m = len(a)
        n = len(b)
        def get(c):
            c = ord(c) - ord('a')
            c += 25
            c %= 26
            return chr(ord('a') + c)
        nxt = {}
        nxts = [-1] * (m + 1)
        for i in range(m - 1, -1, -1):
            nxts[i] = dict(nxt)
            nxt[a[i]] = i
        nxts[-1] = nxt
        prev = -1
        for c in b:
            x = nxts[prev].get(c, m)
            y = nxts[prev].get(get(c), m)
            prev = min(x, y)
            if prev == m:
                return False
        return True