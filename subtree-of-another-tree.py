class Solution:
    def preorder(self, root, seen):
        res = "#"
        if root:
            l = self.preorder(root.left, seen)
            r = self.preorder(root.right, seen)
            res = f"{root.val}{l}{r}"
            seen.add(res)
        return res
    
    def isSubtree(self, root, subRoot):
        sub = self.preorder(subRoot, set())
        seen = set()
        self.preorder(root, seen)
        return sub in seen