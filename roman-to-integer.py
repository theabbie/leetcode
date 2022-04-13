class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        val = 0
        for i in range(n):
            if i < n - 1 and sym[s[i]] < sym[s[i + 1]]:
                val -= sym[s[i]]
            else:
                val += sym[s[i]]
        return val