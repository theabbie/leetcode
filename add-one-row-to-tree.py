# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val = val, left = root)
        nodes = deque([(root, 1)])
        while len(nodes) > 0:
            curr, d = nodes.pop()
            if curr:
                if d == depth - 1:
                    l = curr.left
                    r = curr.right
                    curr.left = TreeNode(val)
                    curr.left.left = l
                    curr.right = TreeNode(val)
                    curr.right.right = r
                else:
                    nodes.appendleft((curr.left, d + 1))
                    nodes.appendleft((curr.right, d + 1))
        return root