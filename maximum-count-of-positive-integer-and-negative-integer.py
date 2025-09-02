class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        for el in nums:
            if el < 0:
                neg += 1
            if el > 0:
                pos += 1
        return max(pos, neg)