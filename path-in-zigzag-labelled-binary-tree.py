class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        p = pow(2, label.bit_length() - 1)
        while p >= 1:
            res.append(label)
            p //= 2
            label = 3 * p - label // 2 - 1
        res.reverse()
        return res