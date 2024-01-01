class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        res = []
        v = []
        c = []
        for i in range(n - 1, -1, -1):
            if s[i] in "aeiouAEIOU":
                v.append(s[i])
            else:
                c.append(s[i])
        v.sort(reverse = True)
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                res.append(v.pop())
            else:
                res.append(c.pop())
        return "".join(res)