# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minVal = float('-inf'), maxVal = float('inf')) -> bool:
        if root:
            if root.val <= minVal or root.val >= maxVal:
                return False
            if not self.isValidBST(root.left, minVal = minVal, maxVal = min(maxVal, root.val)) or not self.isValidBST(root.right, minVal = max(minVal, root.val), maxVal = maxVal):
                return False
        return True