class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        rem = k
        res = []
        for c in s:
            val = ord(c) - ord('a')
            for curr in range(26):
                dist = abs(val - curr)
                dist = min(dist, 26 - dist)
                if dist <= rem:
                    res.append(chr(ord('a') + curr))
                    rem -= dist
                    break
        return "".join(res)