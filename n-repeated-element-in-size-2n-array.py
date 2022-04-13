from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter(nums)
        for k in ctr:
            if 2 * ctr[k] == n:
                return k