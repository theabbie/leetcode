class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if root.val not in self.dup:
                heapq.heappush(self.heap, root.val)
                self.dup.add(root.val)
            self.inorder(root.right)
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.heap = []
        self.dup = set()
        self.inorder(root)
        first = heapq.heappop(self.heap)
        if len(self.heap) > 0:
            second = heapq.heappop(self.heap)
            return second
        return -1
