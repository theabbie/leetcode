class Solution:
    def clean(self, root, curr, limit):
        if not root:
            return (None, float('-inf'))
        root.left, lsum = self.clean(root.left, curr + root.val, limit)
        root.right, rsum = self.clean(root.right, curr + root.val, limit)
        p = max(lsum, rsum)
        if p == float('-inf'):
            p = 0
        msum = root.val + p
        if curr + msum < limit:
            return (None, msum)
        return (root, msum)
    
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return self.clean(root, 0, limit)[0]