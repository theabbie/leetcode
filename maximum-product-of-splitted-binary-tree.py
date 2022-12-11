class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        M = 10 ** 9 + 7
        self.p = 0
        def inorder(r, t = None):
            res = 0
            if r:
                res += inorder(r.left, t)
                res += r.val
                res += inorder(r.right, t)
                if t != None:
                    self.p = max(self.p, res * (t - res))
            return res
        total = inorder(root)
        inorder(root, total)
        return self.p % M