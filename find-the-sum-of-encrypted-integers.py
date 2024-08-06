class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            ctr = 0
            d = 0
            while el:
                d = max(d, el % 10)
                el //= 10
                ctr += 1
            x = 0
            for _ in range(ctr):
                x = 10 * x + d
            res += x
        return res