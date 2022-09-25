class Solution:
    def po(self, root):
        if root:
            return [root.val] + self.po(root.left) + self.po(root.right)
        return []
    
    def preorder(self, root, voyage):
        if root:
            self.i += 1
            valid = True
            if root.left:
                if self.i >= len(voyage):
                    return
                if root.left.val != voyage[self.i]:
                    root.left, root.right = root.right, root.left
                    valid = False
                self.preorder(root.left, voyage)
            if root.right:
                if self.i >= len(voyage):
                    return
                if root.right.val != voyage[self.i]:
                    root.left, root.right = root.right, root.left
                    valid = False
                self.preorder(root.right, voyage)
            if not valid:
                self.res.append(root.val)
    
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        n = len(voyage)
        self.i = 0
        self.res = []
        self.preorder(root, voyage)
        if self.po(root) != voyage:
            return [-1]
        return self.res