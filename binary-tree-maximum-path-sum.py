# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathsum(self, root):
        if root:
            l = self.pathsum(root.left)
            r = self.pathsum(root.right)
            self.msum = max(self.msum, root.val, l + root.val, root.val + r, l + root.val + r)
            return max(root.val, root.val + l, root.val + r)
        return float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.msum = float('-inf')
        self.pathsum(root)
        return self.msum