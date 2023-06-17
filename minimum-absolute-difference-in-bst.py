class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if self.latest != None:
                self.currMin = min(self.currMin, root.val - self.latest)
            self.latest = root.val
            self.inorder(root.right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.currMin = float('inf')
        self.latest = None
        self.inorder(root)
        return self.currMin