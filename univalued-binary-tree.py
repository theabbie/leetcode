# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if self.latest != None:
                if root.val != self.latest:
                    self.uni = False
            self.latest = root.val
            self.inorder(root.right)
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.latest = None
        self.uni = True
        self.inorder(root)
        return self.uni