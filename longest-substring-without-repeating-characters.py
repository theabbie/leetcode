class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i
        longest = 0
        n = len(s)
        dup = {}
        while j < n:
            if s[j] not in dup:
                dup[s[j]] = j
                j += 1
                longest = max(longest, j - i)
            else:
                i = dup[s[j]] + 1
                j = i
                dup = {}
        return longest