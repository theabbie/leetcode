# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        paths = [(root, root.val if root else 0)]
        i = 0
        while i < len(paths):
            curr, currval = paths[i]
            if curr.left or curr.right:
                if curr.left:
                    paths.append((curr.left, 2 * currval + curr.left.val))
                if curr.right:
                    paths.append((curr.right, 2 * currval + curr.right.val))
            else:
                total += currval
            i += 1
        return total