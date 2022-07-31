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
    
    def _update(self, root, i, val):
        if not root:
            return
        if root.start == root.end:
            root.min = val
            return
        mid = (root.start + root.end) // 2
        if i <= mid:
            self.updateVal(root.left, i, val)
        elif i >= mid + 1:
            self.updateVal(root.right, i, val)
        root.total = min(root.left.min, root.right.min)
    
    def update(self, index, val):
        self._update(self.root, index, val)
    
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

arr = [5, 2, 7, 7, 9, 9, 1, 9, 6, 10, 6, 4, 8, 3]

segtree = SegTree(arr)

res = segtree.minRange(9, 12)

print(res)