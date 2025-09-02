class SegmentTree:
    def __init__(self, data):
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        default = (0, float('-inf'), float('-inf'), float('-inf'))
        self.data = [default] * (2 * _size)
        for i in range(self._len):
            val = data[i]
            self.data[_size + i] = (val, val, val, val)
        for i in reversed(range(_size)):
            self.data[i] = self._merge(self.data[2 * i], self.data[2 * i + 1])

    def _merge(self, left, right):
        total_sum = left[0] + right[0]
        max_prefix = max(left[1], left[0] + right[1])
        max_suffix = max(right[2], right[0] + left[2])
        max_subarray_sum = max(left[3], right[3], left[2] + right[1])
        return (total_sum, max_prefix, max_suffix, max_subarray_sum)

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = (value, value, value, value)
        idx >>= 1
        while idx:
            self.data[idx] = self._merge(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def query(self, start, stop):
        start += self._size
        stop += self._size
        left_result = (0, float('-inf'), float('-inf'), float('-inf'))
        right_result = (0, float('-inf'), float('-inf'), float('-inf'))
        while start < stop:
            if start & 1:
                left_result = self._merge(left_result, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                right_result = self._merge(self.data[stop], right_result)
            start >>= 1
            stop >>= 1
        return self._merge(left_result, right_result)

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        segtree = SegmentTree(nums[:])
        pos = {}
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = [-1]
            pos[nums[i]].append(i)
        for el in list(pos):
            pos[el].append(n)
        res = segtree.query(0, n)[3]
        for el in pos:
            poses = pos[el]
            curr = (0, float('-inf'), float('-inf'), float('-inf'))
            for i in range(len(poses) - 1):
                x = poses[i] + 1
                y = poses[i + 1] - 1
                curr = segtree._merge(curr, segtree.query(x, y + 1))
            res = max(res, curr[3])
        return res