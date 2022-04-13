# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        mx = 0
        nodes = [(root, 1)]
        while len(nodes) > 0:
            curr, l = nodes.pop()
            if curr:
                mx = max(mx, l)
                nodes.append((curr.left, 2 * l))
                nodes.append((curr.right, 2 * l + 1))
        return mx