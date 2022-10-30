from collections import Counter

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        ctr = Counter()
        for el in nums:
            ctr[el % space] += 1
        k = max(ctr.values())
        return min(nums, key = lambda el: (float('-inf') if ctr[el % space] == k else float('inf'), el))