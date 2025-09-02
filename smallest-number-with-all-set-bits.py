class Solution:
    def smallestNumber(self, n: int) -> int:
        pw = 1
        while pw - 1 < n:
            pw *= 2
        return pw - 1