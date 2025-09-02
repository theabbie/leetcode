class Solution:
    def recoverFromPreorder(self, traversal: str, d = 0) -> Optional[TreeNode]:
        if len(traversal) == 0:
            return None
        val = 0
        for c in traversal:
            if c == '-':
                break
            val = 10 * val + int(c)
        res = TreeNode(val)
        f = s = len(traversal)
        dash = 0
        for i in range(len(traversal)):
            if traversal[i] == '-':
                dash += 1
                if i + 1 < len(traversal) and dash == d + 1 and traversal[i + 1] != '-':
                    if f == len(traversal):
                        f = i + 1
                    else:
                        s = i + 1
            else:
                dash = 0
        last = len(traversal)
        if s != len(traversal):
            last = s - d - 1
        res.left = self.recoverFromPreorder(traversal[f:last], d + 1)
        res.right = self.recoverFromPreorder(traversal[s:], d + 1)
        return res