class Node:
    def __init__(self, start, end, sum = 0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = sum

class SegTree:
    def __init__(self, nums):
        n = len(nums)
        self.start = 0
        self.end = n - 1
        self.root = self.createTree(0, n - 1, nums)
        
    def createTree(self, start, end, nums):
        if start > end:
            return None
        root = Node(start, end)
        if start == end:
            root.sum = nums[start]
            return root
        mid = (start + end) // 2
        root.left = self.createTree(start, mid, nums)
        root.right = self.createTree(mid + 1, end, nums)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def _update(self, root, start, end, i, val):
        if not root:
            return
        if start == end:
            root.sum += val
            return
        mid = (start + end) // 2
        if i <= mid:
            self._update(root.left, start, mid, i, val)
        else:
            self._update(root.right, mid + 1, end, i, val)
        root.sum = root.left.sum + root.right.sum
    
    def update(self, index, val):
        self._update(self.root, self.start, self.end, index, val)
    
    def _sumRange(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.sum
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self._sumRange(root.left, start, end)
        elif start >= mid + 1:
            return self._sumRange(root.right, start, end)
        else:
            return self._sumRange(root.left, start, mid) + self._sumRange(root.right, mid + 1, end)
    
    def sumRange(self, left, right):
        return self._sumRange(self.root, left, right)

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        segtree = SegTree([0] * (n + 1))
        for i in range(n - k + 1):
            curr = nums[i]
            if segtree.sumRange(0, i) % 2 == 1:
                curr = 1 - curr
            if curr == 0:
                res += 1
                segtree.update(i, 1)
                segtree.update(min(i + k, n), -1)
        for i in range(n - k + 1, n):
            curr = nums[i]
            if segtree.sumRange(0, i) % 2 == 1:
                curr = 1 - curr
            if curr == 0:
                return -1
        return res