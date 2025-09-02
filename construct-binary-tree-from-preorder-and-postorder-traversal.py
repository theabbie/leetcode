class Solution:
    def makeTree(self, preorder, pri, prj, prepos, postorder, poi, poj, postpos):
        if pri >= prj:
            return None
        root = TreeNode(val = preorder[pri])
        if pri + 1 == prj:
            return root
        leftval = preorder[pri + 1]
        rightval = postorder[poj - 2]
        root.left = self.makeTree(preorder, pri + 1, prepos[rightval], prepos, postorder, poi, postpos[leftval] + 1, postpos)
        root.right = self.makeTree(preorder, prepos[rightval], prj, prepos, postorder, postpos[leftval] + 1, poj - 1, postpos)
        return root
    
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        prepos = {}
        postpos = {}
        for i, preval in enumerate(preorder):
            prepos[preval] = i
        for i, postval in enumerate(postorder):
            postpos[postval] = i
        return self.makeTree(preorder, 0, n, prepos, postorder, 0, n, postpos)