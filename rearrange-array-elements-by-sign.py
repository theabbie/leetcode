class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort(key = lambda num: -1 if num < 0 else 1)
        op = []
        for i in range(n // 2):
            op.append(nums[i + n // 2])
            op.append(nums[i])
        return op