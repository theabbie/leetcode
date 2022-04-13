class Solution:
    def canWinNim(self, n: int) -> bool:
        return n != (n >> 2) << 2