class Solution:
    def maxDepth(self, root):
        if root:
            a = 1 + self.maxDepth(root.left)
            b = 1 + self.maxDepth(root.right)
            return max(a, b)
        return -1
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right:
                return self.lcaDeepestLeaves(root.left)
            elif right > left:
                return self.lcaDeepestLeaves(root.right)
            else:
                return root