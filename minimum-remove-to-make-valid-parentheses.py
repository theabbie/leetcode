class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op = set()
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
                op.add(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                    op.add(i)
            else:
                op.add(i)
        for i in stack:
            if i in op:
                op.remove(i)
        return "".join(s[i] for i in sorted(op))