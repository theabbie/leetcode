class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ctr = 0
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if len(stack) == 0 or stack[-1] != '(':
                    ctr += 1
                else:
                    stack.pop()
        ctr += len(stack)
        return ctr