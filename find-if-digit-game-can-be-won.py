class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = sum(nums)
        ss = 0
        for el in nums:
            if el < 10:
                ss += el
        return s - ss != ss