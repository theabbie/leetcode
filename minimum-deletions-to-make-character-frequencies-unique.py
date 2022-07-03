class Solution:
    def minDeletions(self, s: str) -> int:
        ctr = [0] * 26
        for c in s:
            ctr[ord(c) - ord('a')] += 1
        ctr = sorted([f for f in ctr if f != 0])
        n = len(ctr)
        seen = set()
        dels = 0
        for i in range(n):
            while ctr[i] in seen:
                ctr[i] -= 1
                dels += 1
            if ctr[i] > 0:
                seen.add(ctr[i])
        return dels