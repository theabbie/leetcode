# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        l = True
        r = True
        if root:
            if root.left and (root.val != root.left.val or not self.isUnivalTree(root.left)):
                l = False
            if root.right and (root.val != root.right.val or not self.isUnivalTree(root.right)):
                r = False
        return l and r