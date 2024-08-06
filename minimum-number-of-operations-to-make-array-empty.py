from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for f in Counter(nums).values():
            if f == 1:
                return -1
            while f % 3 != 0:
                f -= 2
                res += 1
            res += f // 3
        return res