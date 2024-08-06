class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mn = float('inf')
        for el in nums:
            while len(stack) > 0 and el >= stack[-1][0]:
                stack.pop()
            if len(stack) > 0 and stack[-1][1] < el:
                return True
            stack.append((el, mn))
            mn = min(mn, el)
        return False