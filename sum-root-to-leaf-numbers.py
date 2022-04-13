# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = [(root, root.val)]
        i = 0
        total = 0
        while i < len(paths):
            curr, val = paths[i]
            if curr:
                if not curr.left and not curr.right:
                    total += val
                if curr.left:
                    paths.append((curr.left, 10 * val + curr.left.val))
                if curr.right:
                    paths.append((curr.right, 10 * val + curr.right.val))
            i += 1
        return total