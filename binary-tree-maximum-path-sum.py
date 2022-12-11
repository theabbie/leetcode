class Solution:
    def pathsum(self, root):
        if root:
            l = self.pathsum(root.left)
            r = self.pathsum(root.right)
            self.msum = max(self.msum, root.val, l + root.val, root.val + r, l + root.val + r)
            return max(root.val, root.val + l, root.val + r)
        return float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.msum = float('-inf')
        self.pathsum(root)
        return self.msum