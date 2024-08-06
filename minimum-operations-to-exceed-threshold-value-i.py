class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for el in nums:
            if el < k:
                res += 1
        return res