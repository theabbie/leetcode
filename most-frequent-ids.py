from sortedcontainers import SortedList
from collections import Counter

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        bst = SortedList()
        ctr = Counter()
        res = []
        for i in range(n):
            if ctr[nums[i]] > 0:
                bst.remove(ctr[nums[i]])
            ctr[nums[i]] += freq[i]
            if ctr[nums[i]] > 0:
                bst.add(ctr[nums[i]])
            res.append(bst[-1] if len(bst) > 0 else 0)
        return res