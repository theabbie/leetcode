class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        if s == "a" * n:
            return s[:-1] + "z"
        f = 0
        while f < n and s[f] == "a":
            f += 1
        t = f
        while t < n and s[t] != "a":
            t += 1
        return s[:f] + "".join(chr(ord(c) - 1) for c in s[f:t]) + s[t:]