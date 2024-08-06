from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        even = True
        while q:
            lastodd = float('-inf')
            lasteven = float('inf')
            for _ in range(len(q)):
                curr = q.pop()
                if curr.val & 1:
                    if not even:
                        return False
                    if curr.val <= lastodd:
                        return False
                    lastodd = curr.val
                else:
                    if even:
                        return False
                    if curr.val >= lasteven:
                        return False
                    lasteven = curr.val
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
            even = not even
        return True