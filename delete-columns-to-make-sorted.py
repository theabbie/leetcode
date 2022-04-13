class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        k = len(strs)
        ctr = 0
        for i in range(n):
            col = [s[i] for s in strs]
            if col != sorted(col):
                ctr += 1
        return ctr