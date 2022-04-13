class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vows = {'a',  'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        s = [c for c in s]
        for i in range(n):
            if s[i] in vows:
                stack.append(s[i])
                s[i] = -1
        for i in range(n):
            if s[i] == -1:
                s[i] = stack.pop()
        return "".join(s)