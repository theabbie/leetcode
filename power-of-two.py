class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        while i < n:
            i = i << 1
        return i == n