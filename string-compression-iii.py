class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        res = []
        while i < n:
            ctr = 1
            while i < n - 1 and word[i] == word[i + 1]:
                ctr += 1
                i += 1
            while ctr >= 9:
                res.append(f"9{word[i]}")
                ctr -= 9
            if ctr:
                res.append(f"{ctr}{word[i]}")
            i += 1
        return "".join(res)