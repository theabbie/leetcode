class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        codes = set()
        curr = int(s[0:k], 2)
        codes.add(curr)
        for i in range(n - k):
            curr = (curr << 1) - int(s[i]) * (1 << k) + int(s[i + k])
            codes.add(curr)
        return len(codes) == 1 << k