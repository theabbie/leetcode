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
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right:
                return self.subtreeWithAllDeepest(root.left)
            elif right > left:
                return self.subtreeWithAllDeepest(root.right)
            else:
                return root