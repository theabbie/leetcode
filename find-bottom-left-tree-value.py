class Solution:
    def findBottomLeftValue(self, root) -> int:
        res = (-1, 0, 0)
        def inorder(r, d, w):
            nonlocal res
            if not r:
                return
            inorder(r.left, d + 1, 2 * w)
            res = max(res, (d, -w, r.val))
            inorder(r.right, d + 1, 2 * w + 1)
        inorder(root, 0, 0)
        return res[2]