from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        exists = Counter()
        mlen = 0
        for j in range(n):
            exists[s[j]] += 1
            while i < j and max(exists.values()) > 1:
                exists[s[i]] -= 1
                i += 1
            if max(exists.values()) <= 1:
                mlen = max(mlen, j - i + 1)
        return mlen