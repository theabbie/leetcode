from collections import defaultdict

class Solution:
    def shift(self, c, k):
        return chr(ord('a') + (26 + ord(c) - ord('a') + k) % 26)
    
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        freq = defaultdict(int)
        for l, r, d in shifts:
            d = 2 * d - 1
            freq[l] += d
            freq[r + 1] -= d
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        return "".join([self.shift(s[i], freq[i]) for i in range(n)])