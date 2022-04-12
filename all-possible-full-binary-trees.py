# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        trees = []
        if n == 1:
            return [TreeNode()]
        for i in range(1, n, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - i - 1)
            for left in lefts:
                for right in rights:
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees