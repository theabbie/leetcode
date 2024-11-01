class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(r):
            if not r:
                return (0, True)
            ls, lp = dfs(r.left)
            rs, rp = dfs(r.right)
            curr = lp and rp and ls == rs
            if curr:
                res.append(ls + rs + 1)
            return (ls + rs + 1, curr)
        dfs(root)
        res.sort(reverse = True)
        return res[k - 1] if k <= len(res) else -1