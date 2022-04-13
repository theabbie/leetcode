class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        ctr = 0
        for i in range(n):
            if s[i] == " ":
                ctr += 1
                if ctr == k:
                    return s[:i]
        return s