# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        nodes = [(root, root.val, root.val)]
        mdiff = 0
        while len(nodes) > 0:
            curr, currmin, currmax = nodes.pop()
            mdiff = max(mdiff, currmax - currmin)
            if curr.left:
                nodes.append((curr.left, min(currmin, curr.left.val), max(currmax, curr.left.val)))
            if curr.right:
                nodes.append((curr.right, min(currmin, curr.right.val), max(currmax, curr.right.val)))
        return mdiff