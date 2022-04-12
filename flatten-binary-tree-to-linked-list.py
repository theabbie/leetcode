# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            temp = root.right
            root.right = self.flatten(root.left)
            root.left = None
            curr = root
            while curr and curr.right:
                curr = curr.right
            curr.right = self.flatten(temp)
        return root