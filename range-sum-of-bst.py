class Solution:
    def inorder(self, root, low, high):
        if root:
            if root.val >= low:
                self.inorder(root.left, low, high)
            if root.val >= low and root.val <= high:
                self.total += root.val
            if root.val <= high:
                self.inorder(root.right, low, high)
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        self.inorder(root, low, high)
        return self.total