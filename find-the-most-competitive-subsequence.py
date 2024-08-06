class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[i] < nums[stack[-1]] and len(stack) + n - i - 1 >= k:
                stack.pop()
            stack.append(i)
        while len(stack) > k:
            stack.pop()
        return [nums[i] for i in stack]