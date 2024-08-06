class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        odds = 0
        for el in nums:
            curr = 0
            while el:
                if el & 1:
                    el -= 1
                    odds += 1
                else:
                    el //= 2
                    curr += 1
            res = max(res, curr)
        res += odds
        return res