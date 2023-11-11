class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ctr = [0] * 32
        for el in nums:
            for b in range(32):
                if el & (1 << b):
                    ctr[b] += 1
        return sum(1 << b for b in range(32) if ctr[b] >= k)