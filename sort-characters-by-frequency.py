class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        return "".join([c * k for k, c in sorted([(value, key) for key, value in freq.items()], reverse = True)])