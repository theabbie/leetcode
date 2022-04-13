class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ctr = {}
        for c in t:
            ctr[c] = ctr.get(c, 0) + 1
        for c in s:
            ctr[c] -= 1
            if ctr[c] == 0:
                del ctr[c]
        return list(ctr)[0]
            