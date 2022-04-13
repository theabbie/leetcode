class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vows = {"a", "e", "i", "o", "u"}
        initVowels = 0
        vowelsTill = [initVowels]
        for c in word:
            if c in vows:
                initVowels += 1
            vowelsTill.append(initVowels)
        total = 0
        for i in range(n, -1, -1):
            total += (2 * i - n) * vowelsTill[i]
        return total