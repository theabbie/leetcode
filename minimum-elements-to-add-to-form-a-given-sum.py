import math

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = goal - sum(nums)
        return math.ceil(abs(diff) / limit)