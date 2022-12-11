class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def inorder(r, l, left):
            if r:
                ll = 1
                rl = 1
                if left:
                    rl = l + 1
                elif left != None:
                    ll = l + 1
                inorder(r.left, ll, True)
                self.res = max(self.res, l)
                inorder(r.right, rl, False)
        inorder(root, 0, None)
        return self.res