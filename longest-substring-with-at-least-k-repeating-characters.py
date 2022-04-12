class Solution:
    def lstr(self, s, beg, end, k):
        if end - beg < k:
            return 0
        ctr = [0] * 26
        for i in range(beg, end):
            ctr[ord(s[i]) - ord('a')] += 1
        for i in range(beg, end):
            if ctr[ord(s[i]) - ord('a')] < k:
                return max(self.lstr(s, beg, i, k), self.lstr(s, i + 1, end, k))
        return end - beg
        
    
    def longestSubstring(self, s: str, k: int) -> int:
        return self.lstr(s, 0, len(s), k)