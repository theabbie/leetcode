class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            if word[i] in "aeiou":
                res += (i + 1) * (len(word) - i)
        return res