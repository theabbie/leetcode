class Solution:
    def getPos(self, s, lpal, i, n):
        if i == n:
            return [[]]
        res = []
        for l in lpal[i]:
            curr = s[i:i+l]
            val = self.getPos(s, lpal, i + l, n)
            res += [[curr] + v for v in val]
        return res
    
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        lpal = [[] for _ in range(n)]
        prevpal = [True] * n
        pal = [False] * n
        for i in range(1, n + 1):
            for j in range(i - 1, n):
                pal[j] = True
            l = 1
            while l <= i:
                if i >= 2 and i - l < n - 1:
                    pal[i - l] = s[i - l] == s[i - 1] and prevpal[i - l + 1]
                if pal[i - l]:
                    lpal[i - l].append(l)
                l += 1
            prevpal, pal = pal, prevpal
        return self.getPos(s, lpal, 0, len(s))