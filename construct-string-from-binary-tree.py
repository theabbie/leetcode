# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode], isLeft = False, isRight = False) -> str:
        if root.left and root.right:
            return "{}({})({})".format(root.val, self.tree2str(root.left), self.tree2str(root.right))
        if root.left:
            return "{}({})".format(root.val, self.tree2str(root.left))
        if root.right:
            return "{}()({})".format(root.val, self.tree2str(root.right))
        return "{}".format(root.val)