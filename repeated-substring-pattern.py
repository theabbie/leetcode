class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for l in range(1, 1 + (n // 2)):
            valid = True
            prev = None
            for i in range(0, n, l):
                if prev and prev != s[i:i+l]:
                    valid = False
                    break
                prev = s[i:i+l]
            if valid:
                return True
        return False