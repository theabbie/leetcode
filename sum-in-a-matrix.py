class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            nums[i].sort()
        mx = [0] * n
        for i in range(m):
            for j in range(n):
                mx[j] = max(mx[j], nums[i][j])
        return sum(mx)