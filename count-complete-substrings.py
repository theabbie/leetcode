from collections import *

class Solution:
    def smallK(self, s, k):
        n = len(s)
        res = 0
        for i in range(n):
            j = i
            ctr = Counter()
            mx = 0
            nonzerokvals = 0
            while j < n and mx <= k:
                nonzerokvals -= int(ctr[s[j]] != 0 and ctr[s[j]] != k)
                ctr[s[j]] += 1
                nonzerokvals += int(ctr[s[j]] != 0 and ctr[s[j]] != k)
                if nonzerokvals == 0:
                    res += 1
                mx = max(mx, ctr[s[j]])
                j += 1
        return res
    
    def largeK(self, s, k):
        n = len(s)
        res = 0
        l = k
        while l <= n:
            ctr = Counter()
            nonzerokvals = 0
            for i in range(n):
                nonzerokvals -= int(ctr[s[i]] != 0 and ctr[s[i]] != k)
                ctr[s[i]] += 1
                nonzerokvals += int(ctr[s[i]] != 0 and ctr[s[i]] != k)
                if i >= l:
                    nonzerokvals -= int(ctr[s[i - l]] != 0 and ctr[s[i - l]] != k)
                    ctr[s[i - l]] -= 1
                    nonzerokvals += int(ctr[s[i - l]] != 0 and ctr[s[i - l]] != k)
                if i >= l - 1:
                    if nonzerokvals == 0:
                        res += 1
            l += k
        return res
    
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        res = 0
        j = 0
        while j < n:
            ctr = 1
            while j < n - 1 and abs(ord(word[j]) - ord(word[j+1])) <= 2:
                ctr += 1
                j += 1
            if k * k <= ctr:
                res += self.smallK(word[j-ctr+1:j+1], k)
            else:
                res += self.largeK(word[j-ctr+1:j+1], k)
            j += 1
        return res