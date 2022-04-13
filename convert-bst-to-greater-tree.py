# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def revinorder(self, root):
        if root:
            self.revinorder(root.right)
            self.curr += root.val
            root.val = self.curr
            self.revinorder(root.left)
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.curr = 0
        self.revinorder(root)
        return root