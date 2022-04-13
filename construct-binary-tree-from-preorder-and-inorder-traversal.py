# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeRec(self, inorder, root):
        if len(inorder) > 0:
            currRoot = min((i for i in range(len(inorder))), key = lambda x: self.valIndex[inorder[x]])
            root.val = inorder[currRoot]
            if currRoot > 0:
                root.left = TreeNode()
                self.buildTreeRec(inorder[:currRoot], root.left)
            if currRoot < len(inorder) - 1:
                root.right = TreeNode()
                self.buildTreeRec(inorder[currRoot + 1 :], root.right)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        n = len(inorder)
        self.valIndex = {}
        for i, item in enumerate(preorder):
            self.valIndex[item] = i
        self.buildTreeRec(inorder, root)
        return root