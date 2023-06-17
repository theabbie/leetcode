from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = Counter(nums)
        curr = Counter()
        res = [0] * n
        for i in range(n):
            curr[nums[i]] += 1
            l = r = 0
            for el in total:
                if total[el] - curr[el] > 0:
                    r += 1
                if curr[el] > 0:
                    l += 1
            res[i] = l - r
        return res