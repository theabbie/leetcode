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
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        q = len(queries)
        for i in range(n):
            nums1[i] = (nums1[i], i)
            nums2[i] = (nums2[i], i)
        nums1.sort()
        res = [-1] * q
        for i in range(q):
            queries[i].append(i)
        queries.sort(reverse = True)
        i = n - 1
        vals = set()
        segtree = SegTree(10 ** 9, func = max, init = float('-inf'))
        for x, y, pos in queries:
            while i >= 0 and nums1[i][0] >= x:
                segtree.update(nums2[nums1[i][1]][0], nums1[i][0] + nums2[nums1[i][1]][0])
                i -= 1
            currval = segtree.query(y, 10 ** 9)
            if currval != float('-inf'):
                res[pos] = max(res[pos], currval)
        return res