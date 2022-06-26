class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        changed = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                changed = True
                prev = float('-inf')
                if i > 0:
                    prev = nums[i - 1]
                if prev <= nums[i + 1]:
                    nums[i] = prev
                else:
                    nums[i + 1] = nums[i]
        return True