class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] = max(x[j], x[i])

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [0] * n
        dec = [0] * n
        M = max(nums)
        inctree = FenwickTree([0] * (M + 1))
        dectree = FenwickTree([0] * (M + 1))
        for i in range(n):
            inc[i] = 1 + dectree.query(nums[i])
            dec[i] = 1 + inctree.query(M - nums[i])
            inctree.update(M - nums[i], inc[i])
            dectree.update(nums[i], dec[i])
        return max(max(inc), max(dec))