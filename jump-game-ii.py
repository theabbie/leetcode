class Node:
    def __init__(self, start, end, min = float('inf')):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.min = min

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
            root.min = nums[start]
            return root
        mid = (start + end) // 2
        root.left = self.createTree(start, mid, nums)
        root.right = self.createTree(mid + 1, end, nums)
        root.min = min(root.left.min, root.right.min)
        return root
    
    def _update(self, root, start, end, i, val):
        if not root:
            return
        if start == end:
            root.min = val
            return
        mid = (start + end) // 2
        if i <= mid:
            self._update(root.left, start, mid, i, val)
        else:
            self._update(root.right, mid + 1, end, i, val)
        root.min = min(root.left.min, root.right.min)
    
    def update(self, index, val):
        self._update(self.root, self.start, self.end, index, val)
    
    def _minRange(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.min
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self._minRange(root.left, start, end)
        elif start >= mid + 1:
            return self._minRange(root.right, start, end)
        else:
            return min(self._minRange(root.left, start, mid), self._minRange(root.right, mid + 1, end))
    
    def minRange(self, left, right):
        return self._minRange(self.root, left, right)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [float('inf')] * n
        jumps[n - 1] = 0
        segtree = SegTree(jumps)
        for i in range(n - 2, -1, -1):
            if nums[i] > 0:
                jumps[i] = 1 + segtree.minRange(i + 1, min(i + nums[i], n - 1))
            segtree.update(i, jumps[i])
        return jumps[0]