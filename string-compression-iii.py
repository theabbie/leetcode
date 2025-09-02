class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        n = len(word)
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and word[i] == word[i + 1]:
                i += 1
                ctr += 1
            while ctr:
                d = min(ctr, 9)
                res.append(f"{d}{word[i]}")
                ctr -= d
            i += 1
        return "".join(res)