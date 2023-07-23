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
    def reversePairs(self, nums: List[int]) -> int:
        mp = {}
        for el in nums:
            mp[el] = mp[2 * el + 1] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        fw = FenwickTree([0] * (len(mp) + 1))
        res = 0
        for el in nums:
            res += fw.query(len(mp) + 1) - fw.query(mp[2 * el + 1])
            fw.update(mp[el], 1)
        return res