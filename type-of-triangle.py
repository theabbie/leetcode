class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] == nums[2]:
            return "equilateral"
        if len(set(nums)) == 3:
            return "scalene"
        return "isosceles"