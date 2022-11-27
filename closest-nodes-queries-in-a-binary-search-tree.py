import bisect

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        def inorder(root):
            if root:
                inorder(root.left)
                vals.append(root.val)
                inorder(root.right)
        inorder(root)
        res = []
        for q in queries:
            i = bisect.bisect_left(vals, q)
            res.append([-1, -1])
            if i < len(vals) and vals[i] <= q:
                res[-1][0] = vals[i]
            elif i > 0 and vals[i - 1] <= q:
                res[-1][0] = vals[i - 1]
            if i < len(vals) and vals[i] >= q:
                res[-1][1] = vals[i]
        return res