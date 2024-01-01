class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0
        for i in range(len(s)):
            if int(s[i]) == i % 2:
                a += 1
            else:
                b += 1
        return min(a, b)