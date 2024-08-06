class Solution:
    def reverseParentheses(self, s: str) -> str:
        def solve(x):
            n = len(x)
            stack = []
            for i in range(n):
                if x[i] == '(':
                    stack.append(i)
                if x[i] == ')':
                    p = stack.pop()
                    return solve(x[:p] + solve(x[p+1:i])[::-1] + x[i+1:])
            return x
        return solve(s)