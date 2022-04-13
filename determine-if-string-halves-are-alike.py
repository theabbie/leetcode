class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        f = len([i for i in range(n // 2) if s[i] in vowels])
        s = len([i for i in range(n // 2, n) if s[i] in vowels])
        return f == s