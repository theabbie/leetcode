class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        res = 0
        mx = float('-inf')
        for el in nums:
            if el >= mx:
                mx = el
                res += 1
        return res