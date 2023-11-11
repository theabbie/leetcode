class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        minsofar = nums[:]
        for i in range(1, n):
            minsofar[i] = min(minsofar[i], minsofar[i - 1])
        for i in range(n):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if len(stack) > 0 and stack[-1] > 0 and minsofar[stack[-1] - 1] < nums[i]:
                return True
            stack.append(i)
        return False