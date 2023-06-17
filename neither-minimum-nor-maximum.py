class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)
        for el in nums:
            if el != minn and el != maxx:
                return el
        return -1