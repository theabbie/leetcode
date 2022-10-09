class Solution:
    def inorder(self, root, curr):
        if root:
            curr -= root.val
            if not root.left and not root.right and curr == 0:
                self.res = True
            self.inorder(root.left, curr)
            self.inorder(root.right, curr)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        self.inorder(root, targetSum)
        return self.res