class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        xor = 0
        for i in range(1, n + 2):
            xor ^= i
        currxor = 0
        for i in range(1, n, 2):
            currxor ^= encoded[i]
        res = [xor ^ currxor]
        for el in encoded:
            res.append(res[-1] ^ el)
        return res