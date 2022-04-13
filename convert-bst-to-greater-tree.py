# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, vals):
        if root:
            self.inorder(root.left, vals)
            vals.append(root.val)
            self.inorder(root.right, vals)
    
    def update(self, root, vals):
        if root:
            self.update(root.left, vals)
            root.val = vals[self.i]
            self.i += 1
            self.update(root.right, vals)
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []
        self.inorder(root, vals)
        n = len(vals)
        currSum = 0
        sumVals = []
        for i in range(n - 1, -1, -1):
            currSum += vals[i]
            sumVals.insert(0, currSum)
        self.i = 0
        self.update(root, sumVals)
        return root