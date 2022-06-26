class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        vals = [0 for _ in range(32)]
        for b in range(32):
            for i in range(n):
                if nums[i] & 1 << b:
                    vals[b] += 1
        total = 0
        for i in range(32):
            if vals[i] > 0:
                total += 1 << i
        return total