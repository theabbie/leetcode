class Solution:
    def check(self, root):
        maxval, minval, valid = float('-inf'), float('inf'), True
        if root:
            lmax, lmin, lvalid = self.check(root.left)
            rmax, rmin, rvalid = self.check(root.right)
            maxval = max(maxval, lmax, rmax, root.val)
            minval = min(minval, lmin, rmin, root.val)
            valid = lvalid and rvalid and lmax < root.val < rmin
        return maxval, minval, valid
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root)[2]