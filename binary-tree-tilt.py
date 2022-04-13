# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfTree(self, root):
        if root:
            return root.val + self.sumOfTree(root.left) + self.sumOfTree(root.right)
        return 0
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root:
            l = self.sumOfTree(root.left)
            r = self.sumOfTree(root.right)
            return abs(l - r) + self.findTilt(root.left) + self.findTilt(root.right)
        else:
            return 0