# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root:
            a = 1 + self.maxDepth(root.left)
            b = 1 + self.maxDepth(root.right)
            return max(a, b)
        return -1
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root:
            h = self.maxDepth(root)
            a = self.maxDepth(root.left) == h - 1
            b = self.maxDepth(root.right) == h - 1
            if a and b:
                return root
            if a:
                return self.subtreeWithAllDeepest(root.left)
            if b:
                return self.subtreeWithAllDeepest(root.right)