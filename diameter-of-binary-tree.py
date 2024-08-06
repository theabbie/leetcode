class Solution:
    def maxDepth(self, root):
        if not root:
            return -1
        a = 1 + self.maxDepth(root.left)
        b =  1 + self.maxDepth(root.right)
        self.md = max(self.md, a + b)
        return max(a, b)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.md = float('-inf')
        self.maxDepth(root)
        return self.md