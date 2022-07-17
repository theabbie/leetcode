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
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        h = self.getHeight(root)
        cols = (1 << h) - 1
        res = [(None, float('-inf'))] * h
        nodes = [(root, 0, 0, cols)]
        while len(nodes) > 0:
            curr, l, a, b = nodes.pop()
            if curr:
                i = (a + b) // 2
                if i > res[l][1]:
                    res[l] = (curr.val, i)
                nodes.append((curr.left, l + 1, a, i))
                nodes.append((curr.right, l + 1, i, b))
        return [r[0] for r in res]