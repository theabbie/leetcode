class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m = len(word1)
        n = len(word2)
        a, b = 0, 0
        c, d = 0, 0
        while a < m and c < n:
            if word1[a][b] != word2[c][d]:
                return False
            a, b = a + (b + 1) // len(word1[a]), (b + 1) % len(word1[a])
            c, d = c + (d + 1) // len(word2[c]), (d + 1) % len(word2[c])
        return a >= m and c >= n