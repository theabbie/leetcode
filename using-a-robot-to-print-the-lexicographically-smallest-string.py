class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        smaller = [None] * n
        minchar = "z"
        for i in range(n - 1, -1, -1):
            minchar = min(minchar, s[i])
            if s[i] > minchar:
                smaller[i] = minchar
        res = []
        stack = []
        for i in range(n):
            if smaller[i] != None:
                while len(stack) > 0 and smaller[i] >= stack[-1]:
                    res.append(stack.pop())
                stack.append(s[i])
            else:
                while len(stack) > 0 and s[i] >= stack[-1]:
                    res.append(stack.pop())
                res.append(s[i])
        while len(stack) > 0:
            res.append(stack.pop())
        return "".join(res)