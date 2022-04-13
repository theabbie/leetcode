class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        deletions = set()
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                curr = stack.pop()
                if len(stack) == 0:
                    deletions.update({curr, i})
        return "".join([s[i] for i in range(n) if i not in deletions])