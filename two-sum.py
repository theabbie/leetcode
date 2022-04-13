class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        op = []
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in exists:
                op += [i, exists[compliment]]
                break
            exists[nums[i]] = i
        return op