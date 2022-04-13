# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRoot(self, p, q):
        return max((i for i in range(p, q)), key = lambda x: self.valIndex[self.inorder[x]])
    
    def buildTreeRec(self, p, q):
        if p < q:
            root = TreeNode()
            currRoot = self.getRoot(p, q)
            root.val = self.inorder[currRoot]
            if currRoot > p:
                root.left = TreeNode()
                root.left = self.buildTreeRec(p, currRoot)
            if currRoot < q - 1:
                root.right = TreeNode()
                root.right = self.buildTreeRec(currRoot + 1, q)
            return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        self.inorder = inorder
        self.valIndex = {}
        for i, item in enumerate(postorder):
            self.valIndex[item] = i
        return self.buildTreeRec(0, n)