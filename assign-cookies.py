class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)
        ctr = 0
        i = 0
        for greed in g:
            while i < n and s[i] < greed:
                i += 1
            if i < n:
                i += 1
                ctr += 1
        return ctr