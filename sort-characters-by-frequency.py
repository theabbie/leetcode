import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        nlargest = heapq.nlargest(len(freq), [(value, key) for key, value in freq.items()])
        return "".join([c * k for k, c in nlargest])