def check(root):
    if not root:
        return (True, 0)
    lvalid, lh = check(root.left)
    rvalid, rh = check(root.right)
    return lvalid and rvalid and abs(lh - rh) <= 1, 1 + max(lh, rh)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check(root)[0]