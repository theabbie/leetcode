# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxRob(self, root: Optional[TreeNode], pos, canLoot = True) -> int:
        if (pos, canLoot) in self.cache:
            return self.cache[(pos, canLoot)]
        maxLoot = 0
        if root:
            if canLoot:
                l = self.maxRob(root.left, 2 * pos, canLoot = False)
                r = self.maxRob(root.right, 2 * pos + 1, canLoot = False)
                maxLoot = max(maxLoot, root.val + l + r)
            l = self.maxRob(root.left, 2 * pos, canLoot = True)
            r = self.maxRob(root.right, 2 * pos + 1, canLoot = True)
            maxLoot = max(maxLoot, l + r)
        self.cache[(pos, canLoot)] = maxLoot
        return maxLoot
    
    def rob(self, root: Optional[TreeNode], canLoot = True) -> int:
        self.cache = {}
        return self.maxRob(root, 1, canLoot = True)