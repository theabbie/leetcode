import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ctr = 0
        for num in nums:
            if int(math.log10(num)) & 1:
                ctr += 1
        return ctr