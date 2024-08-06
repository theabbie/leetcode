from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        M = max(ctr.values())
        res = 0
        for el in ctr:
            if ctr[el] == M:
                res += M
        return res