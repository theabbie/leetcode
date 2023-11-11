from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter(nums)
        res = 0
        for el in ctr:
            curr = ctr[el]
            if curr == 1:
                return -1
            while curr >= 2 and curr % 3 != 0:
                curr -= 2
            res += curr // 3
            res += (ctr[el] - curr) // 2
        return res