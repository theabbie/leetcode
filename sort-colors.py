class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r, w, b = 0, 0, 0
        for c in nums:
            if c == 0:
                r += 1
            if c == 1:
                w += 1
            if c == 2:
                b += 1
        for i in range(r + w + b):
            if i < r:
                nums[i] = 0
            if i >= r and i < r + w:
                nums[i] = 1
            if i >= r + w and i < r + w + b:
                nums[i]  = 2