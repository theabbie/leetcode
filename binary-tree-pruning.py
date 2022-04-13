# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasOne(self, root):
        if root:
            if root.val == 1:
                return True
            if self.hasOne(root.left) or self.hasOne(root.right):
                return True
        return False
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.hasOne(root):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root