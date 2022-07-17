# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes = [(root, 0, None)]
        i = 0
        xh, xp, yh, yp = [None] * 4
        while i < len(nodes):
            curr, l, parent = nodes[i]
            if curr:
                if curr.val == x:
                    xh = l
                    xp = parent
                if curr.val == y:
                    yh = l
                    yp = parent
                nodes.append((curr.left, l + 1, curr.val))
                nodes.append((curr.right, l + 1, curr.val))
            i += 1
        return xh == yh and xp != yp