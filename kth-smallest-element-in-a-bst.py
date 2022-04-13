# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    smallest = []
    
    def inorder(self, root, k):
        if root:
            self.inorder(root.left, k)
            self.smallest.append(root.val)
            if len(self.smallest) == k:
                return
            self.inorder(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = []
        self.inorder(root, k)
        return self.smallest[k - 1]