from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        x = Counter(nums)
        return max(s - 2 * el for el in x if (s - 2 * el) in x and (el != s - 2 * el or x.get(el, 0) > 1))