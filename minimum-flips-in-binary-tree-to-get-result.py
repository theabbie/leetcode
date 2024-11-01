class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        op = lambda x, y, o: [x or y, x and y, x ^ y][o - 2]
        @lru_cache(maxsize = None)
        def dp(r, val):
            if not r.left and not r.right:
                return int(r.val != val)
            if r.val == 5:
                return dp(r.left or r.right, not val)
            res = float('inf')
            for x in [False, True]:
                for y in [False, True]:
                    if op(x, y, r.val) == val:
                        res = min(res, dp(r.left, x) + dp(r.right, y))
            return res
        return dp(root, result)