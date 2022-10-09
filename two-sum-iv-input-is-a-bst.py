class Solution:
    def inorder(self, root, k):
        if root and not self.possible:
            self.inorder(root.left, k)
            if (k - root.val) in self.exists:
                self.possible = True
            self.exists.add(root.val)
            self.inorder(root.right, k)
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.possible = False
        self.exists = set()
        self.inorder(root, k)
        return self.possible