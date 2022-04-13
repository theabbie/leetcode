class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        dist = 0
        ctr = [0] * 26
        for i in range(3):
            ctr[ord(s[i]) - ord('a')] += 1
        for i in range(n - 3):
            if max(ctr) == 1:
                dist += 1
            ctr[ord(s[i]) - ord('a')] -= 1
            ctr[ord(s[i+3]) - ord('a')] += 1
        if set(ctr) == {0, 1}:
            dist += 1
        return dist