from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
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
        res.sort(reverse = True)
        return res[k - 1] if k <= len(res) else -1