from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
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
            sums.append(s)
        if root:
            root.val = 0
        q = deque([(root, 0)])
        while q:
            r, d = q.pop()
            if not r:
                continue
            s = 0
            if r.left:
                s += r.left.val
                q.appendleft((r.left, d + 1))
            if r.right:
                s += r.right.val
                q.appendleft((r.right, d + 1))
            if r.left:
                r.left.val = sums[d + 1] - s
            if r.right:
                r.right.val = sums[d + 1] - s
        return root