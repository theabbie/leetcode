from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = nums.count(1)
        res = max(k if k & 1 else k - 1, 1)
        ctr = Counter(nums)
        for el in ctr:
            if el != 1:
                curr = 0
                p = 1
                while ctr[pow(el, p)] >= 2:
                    curr += 2
                    if ctr[pow(el, p * 2)] >= 1:
                        res = max(res, curr + 1)
                    p *= 2
        return res