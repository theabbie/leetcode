class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        ctr = 0
        for c in s:
            if c == letter:
                ctr += 1
        return floor(100 * ctr / n)