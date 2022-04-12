class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        op = [first]
        for el in encoded:
            op.append(op[-1] ^ el)
        return op