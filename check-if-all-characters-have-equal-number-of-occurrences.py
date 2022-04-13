class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ctr = {}
        for c in s:
            ctr[c] = ctr.get(c, 0) + 1
        return len(set(ctr.values())) == 1