class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v = 0
        for c in s:
            if c in "aeiou":
                v += 1
        if v == 0:
            return False
        return True