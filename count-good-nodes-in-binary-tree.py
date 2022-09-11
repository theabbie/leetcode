class Solution:
    def goodNodes(self, root, mval = float('-inf')) -> int:
        res = 0
        if root:
            if root.val >= mval:
                res += 1
                mval = root.val
            res += self.goodNodes(root.left, mval)
            res += self.goodNodes(root.right, mval)
        return res