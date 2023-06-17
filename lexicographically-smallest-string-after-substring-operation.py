class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i = 0
        while i < n and s[i] == "a":
            i += 1
        if i == n:
            pos = ord(s[-1]) - ord("a")
            pos = (pos + 25) % 26
            s[-1] = chr(ord("a") + pos)
            return "".join(s)
        j = i + 1
        while j < n and s[j] != "a":
            j += 1
        for k in range(i, j):
            if k < n:
                s[k] = chr(ord(s[k]) - 1)
        return "".join(s)