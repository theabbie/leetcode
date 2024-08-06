class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) > 1 and stack[-2] + stack[-1] + c == "abc":
                stack.pop()
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0