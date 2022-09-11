from collections import defaultdict

class Solution:
    def inorder(self, root, w, h, res):
        if root:
            self.inorder(root.left, w - 1, h + 1, res)
            res[w][h].append(root.val)
            self.inorder(root.right, w + 1, h + 1, res)
    
    def verticalTraversal(self, root):
        res = defaultdict(lambda: defaultdict(list))
        self.inorder(root, 0, 0, res)
        traversal = []
        for w in sorted(res.keys()):
            col = []
            for h in sorted(res[w].keys()):
                col.extend(sorted(res[w][h]))
            traversal.append(col)
        return traversal