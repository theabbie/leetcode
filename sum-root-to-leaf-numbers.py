class Solution:
    def inorder(self, root, val):
        if root:
            newval = val * 10 + root.val
            self.inorder(root.left, newval)
            self.inorder(root.right, newval)
            if not root.left and not root.right:
                self.res += newval
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.inorder(root, 0)
        return self.res