class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        for b in range(32):
            if n & (1 << b):
                if b & 1:
                    odd += 1
                else:
                    even += 1
        return [even, odd]