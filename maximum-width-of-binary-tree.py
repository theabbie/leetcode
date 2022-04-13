# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, l, w):
        if root:
            self.inorder(root.left, l + 1, 2 * w)
            if l in self.levels:
                self.levels[l] = (min(self.levels[l][0], w), max(self.levels[l][1], w))
                self.mwidth = max(self.mwidth, self.levels[l][1] - self.levels[l][0] + 1)
            else:
                self.levels[l] = (w, w)
                self.mwidth = max(self.mwidth, 1)
            self.inorder(root.right, l + 1, 2 * w + 1)
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.levels = {}
        self.mwidth = 0
        self.inorder(root, 0, 0)
        return self.mwidth