class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        ctr = 0
        for el in nums:
            if el % 6 == 0:
                total += el
                ctr += 1
        if ctr == 0:
            return 0
        return total // ctr