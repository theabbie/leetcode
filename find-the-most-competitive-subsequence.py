class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        rem = n - k
        stack = []
        for el in nums:
            while len(stack) > 0 and el < stack[-1] and rem:
                stack.pop()
                rem -= 1
            stack.append(el)
        while rem:
            stack.pop()
            rem -= 1
        return stack