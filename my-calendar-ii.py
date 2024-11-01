from collections import *

class LazySegmentTree:
    def __init__(self, default=0, func=max):
        self._default = default
        self._func = func
        self._len = 1 + 10**9
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = defaultdict(int)
        self.data = defaultdict(int)

    def _push(self, idx):
        q, self._lazy[idx] = self._lazy[idx], 0
        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        start += self._size
        stop += self._size
        self._update(start)
        self._update(stop - 1)
        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

class MyCalendarTwo:
    def __init__(self):
        self.seg = LazySegmentTree()

    def book(self, start: int, end: int) -> bool:
        if self.seg.query(start, end) == 2:
            return False
        self.seg.add(start, end, 1)
        return True