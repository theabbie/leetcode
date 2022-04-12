class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for i in range(n):
            if freq[s[i]] == 1:
                return i
        return -1