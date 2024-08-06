class Solution:
    def numSteps(self, s: str) -> int:
        val = 0
        for c in s:
            val = 2 * val + int(c)
        res = 0
        while val > 1:
            if val & 1:
                val += 1
            else:
                val //= 2
            res += 1
        return res