class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = 1
        maj = nums[0]
        for i in range(1, n):
            if ctr == 0:
                maj = nums[i]
            if nums[i] != maj:
                ctr -= 1
            else:
                ctr += 1
        return maj