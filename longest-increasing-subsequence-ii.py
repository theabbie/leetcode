class SegTreeNode:
    def __init__(self, val):
        self.val = val
    
class SegTree:
    def __init__(self, n, func, init):
        self.nodes = defaultdict(lambda: SegTreeNode(init))
        self.func = func
        self.init = init
        self.beg = 0
        self.end = n

    def query(self, a, b, x = 0, y = None, k = 1):
        if y == None:
            y = self.end
        if b < x or a > y:
            return self.init
        if a <= x and b >= y:
            return self.nodes[k].val
        mid = (x + y) // 2
        l = self.query(a, b, x, mid, 2 * k)
        r = self.query(a, b, mid + 1, y, 2 * k + 1)
        return self.func(l, r)
    
    def update(self, i, val, x = 0, y = None, k = 1):
        if y == None:
            y = self.end
        if x == y:
            self.nodes[k].val = self.func(val, self.nodes[k].val)
            return
        mid = (x + y) // 2
        if i <= mid:
            self.update(i, val, x, mid, 2 * k)
        else:
            self.update(i, val, mid + 1, y, 2 * k + 1)
        self.nodes[k].val = self.func(self.nodes[2 * k].val, self.nodes[2 * k + 1].val)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)
        M = max(nums) + k + 1
        dp = [1] * n
        segtree = SegTree(M, func = max, init = 0)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + segtree.query(nums[i] + 1, nums[i] + k)
            segtree.update(nums[i], dp[i])
        return max(dp)