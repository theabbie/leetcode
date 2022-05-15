class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            l = 0
            for c in candidates:
                if c & (1 << i):
                    l += 1
            res = max(res, l)
        return res