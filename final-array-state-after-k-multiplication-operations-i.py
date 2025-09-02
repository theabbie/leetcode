class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            nums[nums.index(min(nums))] *= multiplier
        return nums