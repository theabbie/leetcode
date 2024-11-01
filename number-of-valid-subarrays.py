class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        r = [n] * n
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                r[stack.pop()] = i
            stack.append(i)
        return sum(r[i] - i for i in range(n))