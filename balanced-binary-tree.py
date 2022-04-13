# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root:
            a = self.getHeight(root.left)
            b = self.getHeight(root.right)
            return 1 + max(a, b)
        return -1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            a = self.getHeight(root.left)
            b = self.getHeight(root.right)
            if abs(a - b) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            return False
        else:
            return True