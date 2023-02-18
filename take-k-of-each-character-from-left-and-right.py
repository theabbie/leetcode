class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        a, b, c = s.count('a'), s.count('b'), s.count('c')
        ctr = [0, 0, 0]
        res = float('inf')
        i = 0
        for j in range(n):
            ctr[ord(s[j]) - ord('a')] += 1
            while i <= j and (a - ctr[0] < k or b - ctr[1] < k or c - ctr[2] < k):
                ctr[ord(s[i]) - ord('a')] -= 1
                i += 1
            if a - ctr[0] >= k and b - ctr[1] >= k and c - ctr[2] >= k:
                res = min(res, n - (j - i + 1))
        if res == float('inf'):
            return -1
        return res