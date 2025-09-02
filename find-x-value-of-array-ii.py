class SegTree:
    def __init__(self, arr, k):
        self.n = len(arr)
        self.k = k
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [None] * (2 * self.size)
        for i in range(self.size):
            if i < self.n:
                tot = arr[i] % k
                freq = [0] * k
                freq[tot] = 1
                self.tree[self.size + i] = (tot, freq)
            else:
                self.tree[self.size + i] = (1, [0] * k)
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])

    def _merge(self, left, right):
        tot = (left[0] * right[0]) % self.k
        freq = [0] * self.k
        for i in range(self.k):
            freq[i] += left[1][i]
        for j in range(self.k):
            freq[(left[0] * j) % self.k] += right[1][j]
        return (tot, freq)

    def update(self, pos, val):
        p = pos + self.size
        tot = val % self.k
        freq = [0] * self.k
        freq[tot] = 1
        self.tree[p] = (tot, freq)
        p //= 2
        while p:
            self.tree[p] = self._merge(self.tree[2 * p], self.tree[2 * p + 1])
            p //= 2

    def query(self, l, r):
        resl = (1, [0] * self.k)
        resr = (1, [0] * self.k)
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                resl = self._merge(resl, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                resr = self._merge(self.tree[r], resr)
            l //= 2
            r //= 2
        res = self._merge(resl, resr)
        return res[1]

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegTree(nums, k)
        res = []
        for i, v, l, x in queries:
            seg.update(i, v)
            res.append(seg.query(l, n)[x])
        return res