# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            a = self.minDepth(root.left)
            b = self.minDepth(root.right)
            if a == 0 or b == 0:
                return a + b + 1
            return 1 + min(a, b)
        return 0