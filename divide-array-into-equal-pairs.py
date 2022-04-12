from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        for num in ctr:
            if ctr[num] & 1:
                return False
        return True