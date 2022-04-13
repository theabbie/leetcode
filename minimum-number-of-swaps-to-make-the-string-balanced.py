class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        err = 0
        for c in s:
            if c == '[':
                stack.append(c)
            elif c == ']':
                if len(stack) > 0:
                    stack.pop()
                else:
                    err += 1
        return (err + 1) // 2