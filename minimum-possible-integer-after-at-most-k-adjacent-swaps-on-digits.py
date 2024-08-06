from collections import defaultdict
from sortedcontainers import SortedList

class SegTree:
    def __init__(self, n):
        self.ctr = defaultdict(int)
        self.init = (float('inf'), n)
        self.vals = defaultdict(lambda: self.init)
        
    def update(self, i, v, x, y, k = 1):
        if x + 1 == y:
            self.ctr[k] = 0 if v == -1 else 1
            self.vals[k] = (float('inf'), i) if v == -1 else (v, i)
            return
        mid = (x + y) // 2
        if i < mid:
            self.update(i, v, x, mid, 2 * k)
        else:
            self.update(i, v, mid, y, 2 * k + 1)
        self.ctr[k] = self.ctr[2 * k] + self.ctr[2 * k + 1]
        self.vals[k] = min(self.vals[2 * k], self.vals[2 * k + 1])
        
    def getMin(self, p, x, y, k = 1):
        if p == 0:
            return self.init
        if x + 1 == y:
            return self.vals[k]
        mid = (x + y) // 2
        res = self.init
        if p >= self.ctr[2 * k]:
            res = min(res, self.vals[2 * k], self.getMin(p - self.ctr[2 * k], mid, y, 2 * k + 1))
        else:
            res = min(res, self.getMin(p, x, mid, 2 * k))
        return res

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        segtree = SegTree(n)
        for i in range(n):
            segtree.update(i, int(num[i]), 0, n)
        w = k + 1
        res = []
        bst = SortedList()
        while len(res) < n:
            val, j = segtree.getMin(min(w, n), 0, n)
            res.append(num[j])
            pos = j - bst.bisect_right(j - 1)
            bst.add(j)
            w -= pos
            segtree.update(j, -1, 0, n)
        return "".join(res)