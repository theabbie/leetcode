# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, l):
        if root:
            self.inorder(root.left, l + 1)
            if not root.left and not root.right:
                if l > self.deepest:
                    self.deepest = l
                    self.deepestsum = root.val
                elif l == self.deepest:
                    self.deepestsum += root.val
            self.inorder(root.right, l + 1)
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.deepest = 0
        self.deepestsum = 0
        self.inorder(root, 0)
        return self.deepestsum