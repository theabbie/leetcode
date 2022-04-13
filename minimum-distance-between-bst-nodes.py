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
                if self.minDiff == None or root.val - self.latest < self.minDiff:
                    self.minDiff = root.val - self.latest
            self.latest = root.val
            self.inorder(root.right)
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDiff = None
        self.latest = None
        self.inorder(root)
        return self.minDiff