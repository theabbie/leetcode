class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        res = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if i + 1 == n or s[i + 1] != ')':
                    res += 1
                else:
                    i += 1
                if not stack:
                    res += 1
                else:
                    stack.pop()
            i += 1
        res += 2 * len(stack)
        return res