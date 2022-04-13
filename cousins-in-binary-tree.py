# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, l, x, y, path):
        if root:
            if root.left:
                self.inorder(root.left, l + 1, x, y, path[-1:] + [root.left.val])
            if root.val == x:
                self.xnode = (l, path[-2] if len(path) >= 2 else None)
            if root.val == y:
                self.ynode = (l, path[-2] if len(path) >= 2 else None)
            if root.right:
                self.inorder(root.right, l + 1, x, y, path[-1:] + [root.right.val])
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.inorder(root, 0, x, y, [root.val])
        return self.xnode[0] == self.ynode[0] and self.xnode[1] != self.ynode[1]