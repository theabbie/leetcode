class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        a,b = divmod(k-n, 25)
        c = max(n-a-1, 0)
        d = n-a-c
        return "a" * c + chr(ord('a') + b) * d + "z" * a