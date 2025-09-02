N = 100000
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * self._size)
        self.data = [default] * (2 * self._size)
        self.data[self._size:self._size + self._len] = data
        for i in range(self._size - 1, 0, -1):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def _push(self, idx):
        q = self._lazy[idx]
        if q:
            self._lazy[2 * idx] += q
            self._lazy[2 * idx + 1] += q
            self.data[2 * idx] += q
            self.data[2 * idx + 1] += q
            self._lazy[idx] = 0

    def _update(self, idx):
        for h in range(idx.bit_length() - 1, 0, -1):
            self._push(idx >> h)

    def _build(self, idx):
        while idx > 1:
            idx >>= 1
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]

    def add(self, l, r, v):
        l0, r0 = l + self._size, r + self._size
        l1, r1 = l0, r0
        while l0 < r0:
            if l0 & 1:
                self._lazy[l0] += v
                self.data[l0] += v
                l0 += 1
            if r0 & 1:
                r0 -= 1
                self._lazy[r0] += v
                self.data[r0] += v
            l0 >>= 1
            r0 >>= 1
        self._build(l1)
        self._build(r1 - 1)

    def query(self, l, r):
        l += self._size
        r += self._size
        self._update(l)
        self._update(r - 1)
        res = self._default
        while l < r:
            if l & 1:
                res = self._func(res, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res = self._func(res, self.data[r])
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maximumCount(self, nums, queries):
        n = len(nums)
        self.nums = [0] * n
        self.pos = defaultdict(lambda: SortedList([-1, n]))
        self.st = LazySegmentTree([0] * (n + 1))
        def update(idx, val):
            old = self.nums[idx]
            if is_prime[old]:
                lst = self.pos[old]
                i = lst.bisect_left(idx)
                prv = lst[i-1]
                nxt = lst[i+1]
                if prv == -1:
                    self.st.add(idx+1, nxt+1, -1)
                if nxt == n:
                    self.st.add(prv+1, idx+1, -1)
                lst.remove(idx)
            self.nums[idx] = val
            if is_prime[val]:
                lst = self.pos[val]
                lst.add(idx)
                i = lst.bisect_left(idx)
                prv = lst[i-1]
                nxt = lst[i+1]
                if prv == -1:
                    self.st.add(idx+1, nxt+1, 1)
                if nxt == n:
                    self.st.add(prv+1, idx+1, 1)
        for i, v in enumerate(nums):
            update(i, v)
        res = []
        for idx, val in queries:
            update(idx, val)
            res.append(self.st.query(1, n))
        return res