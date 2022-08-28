class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)