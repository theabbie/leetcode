class Solution:
    def sumcount(self, root):
        total = 0
        n = 0
        if root:
            ltotal, ln = self.sumcount(root.left)
            rtotal, rn = self.sumcount(root.right)
            total = ltotal + rtotal + root.val
            n = ln + rn + 1
            if root.val == total // n:
                self.ctr += 1
        return (total, n)
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ctr = 0
        self.sumcount(root)
        return self.ctr