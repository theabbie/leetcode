from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MX = min(5 * 10 ** 4, 3 * len(queries)) + 10
        bst = SortedList([0, MX])
        segtree = SegmentTree([0] * (MX + 1))
        res = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                pos = bst.bisect_left(x)
                l = bst[pos - 1]
                r = bst[pos]
                segtree[r] = r - x
                segtree[x] = x - l
                bst.add(x)
            if q[0] == 2:
                x, sz = q[1], q[2]
                pos = bst.bisect_left(x)
                if bst[pos] > x:
                    pos -= 1
                l = bst[pos]
                if x - l >= sz:
                    res.append(True)
                else:
                    res.append(segtree.query(0, x + 1) >= sz)
        return res