class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flat(r):
            if not r:
                return r
            lend = flat(r.left)
            rend = flat(r.right)
            r.right, (lend or r).right, r.left, = r.left, r.right, None
            return rend or lend or r
        flat(root)
        return root