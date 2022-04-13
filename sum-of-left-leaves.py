# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, isLeft):
        if root:
            self.inorder(root.left, True)
            if isLeft and not root.left and not root.right:
                self.total += root.val
            self.inorder(root.right, False)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.inorder(root, False)
        return self.total