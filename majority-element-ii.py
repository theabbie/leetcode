from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ctr = Counter(nums)
        return [el for el in ctr if 3 * ctr[el] > n]