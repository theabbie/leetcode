class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)
        ctr = 0
        for greed in g:
            for i in range(n):
                if s[i] != None:
                    if s[i] >= greed:
                        s[i] = None
                        ctr += 1
                        break
        return ctr