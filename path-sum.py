# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        paths = [(root, root.val if root else 0)]
        i = 0
        while i < len(paths):
            curr, val = paths[i]
            if curr:
                if not curr.left and not curr.right:
                    if val == targetSum:
                        return True
                if curr.left:
                    paths.append((curr.left, val + curr.left.val))
                if curr.right:
                    paths.append((curr.right, val + curr.right.val))
            i += 1
        return False