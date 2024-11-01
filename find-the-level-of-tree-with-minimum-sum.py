from collections import deque

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque([root])
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                r = q.pop()
                if not r:
                    continue
                s += r.val
                if r.left:
                    q.appendleft(r.left)
                if r.right:
                    q.appendleft(r.right)
            res.append(s)
        return res.index(min(res)) + 1