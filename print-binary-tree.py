# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return 0
    
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        h = self.getHeight(root)
        cols = (1 << h) - 1
        rows = h
        op = [["" for i in range(cols)] for j in range(rows)]
        nodes = [(root, 0, 0, cols)]
        while len(nodes) > 0:
            curr, l, a, b = nodes.pop()
            if curr:
                i = (a + b) // 2
                op[l][i] = str(curr.val)
                nodes.append((curr.left, l + 1, a, i))
                nodes.append((curr.right, l + 1, i, b))
        return op