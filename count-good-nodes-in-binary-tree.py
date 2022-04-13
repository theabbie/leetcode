# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        paths = [(root, root.val)]
        ctr = 0
        while len(paths) > 0:
            curr, currmax = paths.pop()
            if curr.val >= currmax:
                ctr += 1
            if curr.left:
                paths.append((curr.left, max(currmax, curr.left.val)))
            if curr.right:
                paths.append((curr.right, max(currmax, curr.right.val)))
        return ctr