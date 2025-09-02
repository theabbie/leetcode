class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(r, left):
            if not r:
                return 0
            if not r.left and not r.right and left:
                return r.val
            return dfs(r.left, True) + dfs(r.right, False)
        return dfs(root, False)