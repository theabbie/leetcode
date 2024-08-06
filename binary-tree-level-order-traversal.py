from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            res.append([])
            for _ in range(len(q)):
                curr = q.pop()
                res[-1].append(curr.val)
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
        return res