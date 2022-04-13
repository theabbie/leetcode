# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, k):
        if root:
            self.inorder(root.left, k)
            self.i += 1
            if self.i == k:
                self.kth = root.val
            self.inorder(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.kth = None
        self.inorder(root, k)
        return self.kth