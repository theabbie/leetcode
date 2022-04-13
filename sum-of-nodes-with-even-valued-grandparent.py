# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        paths = [(root, [root.val] if root else [])]
        i = 0
        total = 0
        while i < len(paths):
            curr, currpath = paths[i]
            if curr:
                if len(currpath) > 2 and currpath[-3] % 2 == 0:
                    total += curr.val
                if curr.left:
                    paths.append((curr.left, currpath + [curr.left.val]))
                if curr.right:
                    paths.append((curr.right, currpath + [curr.right.val]))
            i += 1
        return total