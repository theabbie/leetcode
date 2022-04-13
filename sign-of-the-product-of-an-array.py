class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            curr = 1
            if num < 0:
                curr = -1
            elif num == 0:
                curr = 0
            sign *= curr
        return sign