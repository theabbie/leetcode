from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        return sum([k for k, v in ctr.items() if v == 1])