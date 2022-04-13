from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ctr = Counter(s)
        maxOdd = 0
        evens = 0
        for c in ctr:
            if ctr[c] % 2 == 0:
                evens += ctr[c]
            else:
                evens += ctr[c] - 1
                maxOdd = max(maxOdd, 1)
        return maxOdd + evens