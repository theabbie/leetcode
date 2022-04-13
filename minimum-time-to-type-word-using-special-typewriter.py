class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        t = 0
        for c in word:
            d = abs(ord(c) - ord(curr))
            t += min(d, 26 - d)
            curr = c
        return t + len(word)