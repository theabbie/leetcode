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
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mp = {}
        for el in instructions:
            mp[el] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        M = len(mp)
        fw = FenwickTree([0] * (M + 1))
        res = 0
        for el in instructions:
            res += min(fw.query(mp[el]), fw.query(M + 1) - fw.query(mp[el] + 1))
            res %= MOD
            fw.update(mp[el], 1)
        return res