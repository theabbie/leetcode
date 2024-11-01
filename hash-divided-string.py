class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        ctr = [0] * (n // k)
        for i in range(n):
            ctr[i // k] += ord(s[i]) - ord('a')
            ctr[i // k] %= 26
        return "".join(chr(ord('a') + c) for c in ctr)