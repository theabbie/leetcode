class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        allowed = set(range(n))
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                curr = stack.pop()
                if len(stack) == 0:
                    allowed.remove(curr)
                    allowed.remove(i)
        return "".join([s[i] for i in allowed])