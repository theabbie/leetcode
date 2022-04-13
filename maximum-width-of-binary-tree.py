# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = {}
        nodes = [(root, 0, 0)]
        while len(nodes) > 0:
            curr, w, l = nodes.pop()
            if curr:
                if l in levels:
                    levels[l] = (min(levels[l][0], w), max(levels[l][1], w))
                else:
                    levels[l] = (w, w)
                nodes.append((curr.left, 2 * w, l + 1))
                nodes.append((curr.right, 2 * w + 1, l + 1))
        mwidth = 0
        for l in levels:
            mwidth = max(mwidth, levels[l][1] - levels[l][0] + 1)
        return mwidth