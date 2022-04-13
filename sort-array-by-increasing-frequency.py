from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        return sorted(nums, key = lambda x: (ctr[x], -x))