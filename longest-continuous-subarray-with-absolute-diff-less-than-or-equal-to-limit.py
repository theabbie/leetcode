class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minvals = RangeQuery(nums, min)
        maxvals = RangeQuery(nums, max)
        res = 1
        i = 0
        for j in range(n):
            while maxvals.query(i, j + 1) - minvals.query(i, j + 1) > limit:
                i += 1
            res = max(res, j - i + 1)
        return res