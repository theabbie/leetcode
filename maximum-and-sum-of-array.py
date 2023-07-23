class Solution:
    def maxsum(self, nums, i, n, fmask, smask, numSlots):
        if i >= n:
            return 0
        key = (i, fmask, smask)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for j in range(numSlots):
            if not fmask & (1 << j) or not smask & (1 << j):
                currfmask = fmask
                currsmask = smask
                if not currfmask & (1 << j):
                    currfmask |= 1 << j
                elif not currsmask & (1 << j):
                    currsmask |= 1 << j
                res = max(res, ((j + 1) & nums[i]) + self.maxsum(nums, i + 1, n, currfmask, currsmask, numSlots))
        self.cache[key] = res
        return res
    
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        self.cache = {}
        return self.maxsum(nums, 0, len(nums), 0, 0, numSlots)