class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        M = 10 ** 9 + 7
        aa = a
        bb = b
        for bit in range(n):
            aa &= ~(1 << bit)
            bb &= ~(1 << bit)
        v = a ^ b
        for bit in range(n - 1, -1, -1):
            aa += 1 << bit
            bb += 1 << bit
            if v & (1 << bit):
                if aa <= bb:
                    bb -= 1 << bit
                else:
                    aa -= 1 << bit
        return (aa * bb) % M