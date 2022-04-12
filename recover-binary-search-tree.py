# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, append):
        if root:
            self.inorder(root.left, append)
            if append:
                self.vals.append(root.val)
            else:
                root.val = self.vals[self.i]
                self.i += 1
            self.inorder(root.right, append)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.vals = []
        self.inorder(root, True)
        self.vals.sort()
        self.i = 0
        self.inorder(root, False)