# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = TreeNode(val = val)
        if not root:
            return curr
        if val > root.val:
            curr.left = root
            return curr
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root