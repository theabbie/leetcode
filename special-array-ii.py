from bisect import *

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        p = []
        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                p.append(i)
        return [bisect_right(p, j - 1) - bisect_left(p, i) == 0 for i, j in queries]