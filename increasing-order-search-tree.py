# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, key):
        if root:
            if key <= root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        else:
            root = TreeNode(val = key)
        return root
    
    def insort(self, root):
        if root:
            self.insort(root.left)
            self.newroot = self.insert(self.newroot, root.val)
            self.insort(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newroot = None
        self.insort(root)
        return self.newroot