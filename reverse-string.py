class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]