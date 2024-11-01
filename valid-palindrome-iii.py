class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        @lru_cache(maxsize = None)
        def check(i, j, l):
            if i > j:
                return int(l == 0)
            if j - i + 1 < l:
                return False
            if l == 1:
                return i <= j
            if check(i + 1, j, l) or check(i, j - 1, l):
                return True
            if s[i] == s[j] and check(i + 1, j - 1, l - 2):
                return True
            return False
        return check(0, n - 1, n - k)