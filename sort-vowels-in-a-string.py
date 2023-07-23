class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        vals = []
        for i in range(n):
            if s[i].lower() in "aeiou":
                vals.append(s[i])
        vals.sort(reverse = True)
        for i in range(n):
            if s[i].lower() in "aeiou":
                s[i] = vals.pop()
        return "".join(s)