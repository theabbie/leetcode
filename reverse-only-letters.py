class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        stack = []
        for i in range(n):
            if s[i].islower() or s[i].isupper():
                stack.append(s[i])
                s[i] = -1
        for i in range(n):
            if s[i] == -1:
                s[i] = stack.pop()
        return "".join(s)