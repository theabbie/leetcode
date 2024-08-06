class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        MX = max(nums)
        ctr = [0] * (MX + 2)
        c = collections.Counter(nums)
        for el in c:
            mul = 1
            while el * mul <= MX:
                ctr[el * mul] += c[el] * mul
                ctr[min(el * (mul + 1), MX + 1)] -= c[el] * mul
                mul += 1
        for i in range(MX):
            ctr[i + 1] += ctr[i]
            ctr[i + 1] %= M
        return sum(ctr[el] for el in nums) % M