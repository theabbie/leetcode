class LazySegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.lazy = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def update_range(self, node, start, end, left, right, value):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start > end or start > right or end < left:
            return
        if start >= left and end <= right:
            self.tree[node] += value
            if start != end:
                self.lazy[2 * node] += value
                self.lazy[2 * node + 1] += value
            return
        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, left, right, value)
        self.update_range(2 * node + 1, mid + 1, end, left, right, value)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query_range(self, node, start, end, left, right):
        if start > end or start > right or end < left:
            return float('inf')
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start >= left and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_min = self.query_range(2 * node, start, mid, left, right)
        right_min = self.query_range(2 * node + 1, mid + 1, end, left, right)
        return min(left_min, right_min)

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        last = {}
        secondlast = {}
        ctr = LazySegmentTree([0] * n + [n])
        for i in range(n - 1, -1, -1):
            ctr.update_range(1, 0, n, i + 1, last.get(nums[i], n + 1) - 1, -1)
            ctr.update_range(1, 0, n, last.get(nums[i], n + 1), secondlast.get(nums[i], n + 1) - 1, 1)
            secondlast[nums[i]] = last.get(nums[i], n + 1)
            last[nums[i]] = i + 1
            curr = k - i + ctr.query_range(1, 0, n, i + 1, n)
            ctr.update_range(1, 0, n, i, i, i + curr)
        return ctr.query_range(1, 0, n, 0, 0)