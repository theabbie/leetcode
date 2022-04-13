# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = [(root, 0, 0)]
        leftmost = (0, 0, root.val)
        while len(nodes) > 0:
            curr, w, l = nodes.pop()
            if curr:
                if l > leftmost[1] or (l == leftmost[1] and w < leftmost[0]):
                    leftmost = (w, l, curr.val)
                nodes.append((curr.left, w - 1, l + 1))
                nodes.append((curr.right, w + 1, l + 1))
        return leftmost[2]