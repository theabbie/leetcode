class Solution:
    def distributeCoins(self, root):
        def find(r):
            if not r:
                return 0, 0
            lextra, lval = find(r.left)
            rextra, rval = find(r.right)
            extra = r.val + lextra + rextra - 1
            return extra, lval + rval + abs(extra)
        return find(root)[1]