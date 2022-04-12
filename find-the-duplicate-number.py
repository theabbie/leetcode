class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        curr = nums[0]
        for num in nums[1:]:
            if num == curr:
                return num
            curr = num