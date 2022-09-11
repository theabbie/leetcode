class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        w = [word1, word2]
        k = n
        bigger = word1
        if m < n:
            bigger = word2
            k = m
        ch = lambda i: w[i % 2][i // 2] if i < 2 * k else bigger[i - k]
        return "".join(ch(i) for i in range(m + n))