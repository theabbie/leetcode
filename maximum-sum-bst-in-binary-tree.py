class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def msum(root):
            if not root:
                return 0, float('inf'), float('-inf'), True
            lsum, lmin, lmax, lvalid = msum(root.left)
            rsum, rmin, rmax, rvalid = msum(root.right)
            currsum = lsum + rsum + root.val
            currmin = min(root.val, lmin, rmin)
            currmax = max(root.val, lmax, rmax)
            currvalid = lvalid and rvalid
            if lmax >= root.val or rmin <= root.val:
                currvalid = False
            if currvalid:
                self.res = max(self.res, currsum)
            return currsum, currmin, currmax, currvalid
        msum(root)
        return self.res