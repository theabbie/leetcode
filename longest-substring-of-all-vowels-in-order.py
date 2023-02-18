class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        i = 0
        chars = []
        ctrs = []
        while i < n:
            ctr = 1
            while i < n - 1 and word[i] == word[i + 1]:
                i += 1
                ctr += 1
            chars.append(word[i])
            ctrs.append(ctr)
            i += 1
        res = 0
        m = len(chars)
        for i in range(m - 4):
            if "".join(chars[i:i+5]) == "aeiou":
                res = max(res, sum(ctrs[i:i+5]))
        return res