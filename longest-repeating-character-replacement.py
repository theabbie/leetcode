class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        mlen = 0
        for c in set(s):
            ctr = 0
            i = 0
            j = 0
            while j < n:
                if s[j] != c:
                    ctr += 1
                while ctr > k:
                    if s[i] != c:
                        ctr -= 1
                    i += 1
                mlen = max(mlen, j - i + 1)
                j += 1
        return mlen