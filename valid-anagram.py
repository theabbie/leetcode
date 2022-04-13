class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctr = {}
        for c in s:
            ctr[c] = ctr.get(c, 0) + 1
        for c in t:
            if c in ctr:
                ctr[c] -= 1
            else:
                return False
        for val in ctr.values():
            if val != 0:
                return False
        return True