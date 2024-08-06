class Solution:
    def inorder(self, root, isLeft):
        if root:
            self.inorder(root.left, True)
            if isLeft and not root.left and not root.right:
                self.total += root.val
            self.inorder(root.right, False)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.inorder(root, False)
        return self.total