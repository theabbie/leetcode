class Node:
    def __init__(self, start, end, total = 0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0

class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.root = self.createTree(0, n - 1, nums)
        
    def createTree(self, start, end, nums):
        if start > end:
            return None
        root = Node(start, end)
        if start == end:
            root.total = nums[start]
            return root
        mid = (start + end) // 2
        root.left = self.createTree(start, mid, nums)
        root.right = self.createTree(mid + 1, end, nums)
        root.total = root.left.total + root.right.total
        return root
    
    def updateVal(self, root, i, val):
        if not root:
            return
        if root.start == root.end:
            root.total = val
            return
        mid = (root.start + root.end) // 2
        if i <= mid:
            self.updateVal(root.left, i, val)
        elif i >= mid + 1:
            self.updateVal(root.right, i, val)
        root.total = root.left.total + root.right.total
    
    def update(self, index, val):
        self.updateVal(self.root, index, val)
    
    def getSum(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.total
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.getSum(root.left, start, end)
        elif start >= mid + 1:
            return self.getSum(root.right, start, end)
        else:
            return self.getSum(root.left, start, mid) + self.getSum(root.right, mid + 1, end)
    
    def sumRange(self, left, right):
        return self.getSum(self.root, left, right)