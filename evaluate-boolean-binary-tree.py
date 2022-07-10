# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            l = self.evaluateTree(root.left) == 1
            r = self.evaluateTree(root.right) == 1
            if root.val == 2:
                return l or r
            elif root.val == 3:
                return l and r
            else:
                return root.val == 1
        return False