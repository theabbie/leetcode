class Solution:
    def revinorder(self, root):
        if root:
            self.revinorder(root.right)
            self.curr += root.val
            root.val = self.curr
            self.revinorder(root.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.curr = 0
        self.revinorder(root)
        return root