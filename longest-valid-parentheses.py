class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        mlen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif len(stack) > 0:
                stack.pop()
                if len(stack) > 0:
                    mlen = max(mlen, i - stack[-1])
                else:
                    stack.append(i)
        return mlen