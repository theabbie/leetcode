# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if p or q:
                return False
            return True
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root or not subRoot:
            return False
        if self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)