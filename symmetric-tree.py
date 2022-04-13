# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if p or q:
                return False
            return True
        if p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left):
            return True
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.isMirror(root.left, root.right)
        return True