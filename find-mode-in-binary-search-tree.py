class Solution:
    def inorder(self, root, ctr):
        if root:
            self.inorder(root.left, ctr)
            ctr[root.val] = ctr.get(root.val, 0) + 1
            self.inorder(root.right, ctr)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ctr = {}
        self.inorder(root, ctr)
        maxVal = max(ctr.values())
        return [k for k, v in ctr.items() if v == maxVal]