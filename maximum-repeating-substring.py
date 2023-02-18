class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        res = 0
        for i in range(n):
            j = i
            while j < n and sequence[j] == word[(j - i) % m]:
                j += 1
            res = max(res, (j - i) // m)
        return res