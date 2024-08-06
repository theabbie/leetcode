from collections import defaultdict

M = 10 ** 9 + 7

class SegTree:
    def __init__(self):
        self.tree = defaultdict(lambda: (0, 0, 0, 0))
        
    def merge(self, l, r):
        l_with_f_with_end, l_with_f_without_end, l_without_f_with_end, l_without_f_without_end = l
        r_with_f_with_end, r_with_f_without_end, r_without_f_with_end, r_without_f_without_end = r
        r_end_max = max(r_with_f_with_end, r_without_f_with_end)
        r_without_end_max = max(r_with_f_without_end, r_without_f_without_end)
        return (max(l_with_f_with_end + r_without_f_with_end, l_with_f_without_end + r_end_max), max(l_with_f_with_end + r_without_f_without_end, l_with_f_without_end + r_without_end_max), max(l_without_f_with_end + r_without_f_with_end, l_without_f_without_end + r_end_max), max(l_without_f_with_end + r_without_f_without_end, l_without_f_without_end + r_without_end_max))
        
    def update(self, index, val, i, j, k):
        if i + 1 == j:
            self.tree[k] = (val, 0, 0, 0)
            return
        mid = (i + j) // 2
        if index < mid:
            self.update(index, val, i, mid, 2 * k)
        else:
            self.update(index, val, mid, j, 2 * k + 1)
        self.tree[k] = self.merge(self.tree[2 * k], self.tree[2 * k + 1])
        
    def query(self, x, y, i, j, k):
        if y - 1 < i or x >= j:
            return (0, 0, 0, 0)
        if i >= x and j <= y:
            return self.tree[k]
        mid = (i + j) // 2
        return self.merge(self.query(x, y, i, mid, 2 * k), self.query(x, y, mid, j, 2 * k + 1))

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        res = 0
        segtree = SegTree()
        for i in range(n):
            segtree.update(i, nums[i], 0, n, 1)
        for i, val in queries:
            segtree.update(i, val, 0, n, 1)
            res += max(segtree.query(0, n, 0, n, 1))
            res %= M
        return res