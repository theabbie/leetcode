# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.tree.append(root.val)
            self.inorder(root.right)
            
    def arrToTree(self, arr, i, j):
        if i <= j - 1:
            root = TreeNode()
            mid = (i + j) // 2
            root.val = arr[mid]
            root.left = self.arrToTree(arr, i, mid)
            root.right = self.arrToTree(arr, mid + 1, j)
            return root
        return None
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.tree = []
        self.inorder(root)
        return self.arrToTree(self.tree, 0, len(self.tree))