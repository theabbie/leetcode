class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + nums[i]
        mp = {}
        for el in p:
            mp[el] = mp[el - lower] = mp[el - upper] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        fw = FenwickTree([0] * (len(mp) + 1))
        res = 0
        for el in p:
            res += fw.query(mp[el - lower] + 1) - fw.query(mp[el - upper])
            fw.update(mp[el], 1)
        return res