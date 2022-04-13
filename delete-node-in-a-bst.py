# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, node):
        if root:
            if node:
                if node.val <= root.val:
                    root.left = self.insert(root.left, node)
                else:
                    root.right = self.insert(root.right, node)
        else:
            root = node
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                root = self.insert(root.left, root.right)
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
        else:
            return None