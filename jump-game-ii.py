class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [float('inf')] * n
        jumps[n - 1] = 0
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n and j <= i + nums[i]:
                jumps[i] = min(jumps[i], 1 + jumps[j])
                j += 1
        return jumps[0]