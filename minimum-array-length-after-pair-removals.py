class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 2
        left = nums[:k]
        right = nums[k:]
        res = n
        j = 0
        for el in left:
            while j < len(right) and right[j] == el:
                j += 1
            if j < len(right):
                res -= 2
            j += 1
        return res