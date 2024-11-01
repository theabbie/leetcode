class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for d in b:
            res = pow(res, 10, 1337) * pow(a, d, 1337)
            res %= 1337
        return res