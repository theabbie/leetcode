# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, l):
        if root:
            self.inorder(root.left, l + 1)
            self.levels[l] = self.levels.get(l, 0) + root.val
            self.inorder(root.right, l + 1)
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.levels = {}
        self.inorder(root, 1)
        return -max([(v, -k) for k, v in self.levels.items()])[1]