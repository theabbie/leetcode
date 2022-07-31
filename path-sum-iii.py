# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def count(self, root, currsum, ctr, targetSum):
        if root:
            self.res += ctr[currsum - targetSum]
            ctr[currsum] += 1
            if root.left:
                self.count(root.left, currsum + root.left.val, ctr, targetSum)
            if root.right:
                self.count(root.right, currsum + root.right.val, ctr, targetSum)
            ctr[currsum] -= 1
        else:
            self.res += ctr[currsum - targetSum]
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ctr = defaultdict(int)
        self.res = 0
        ctr[0] = 1
        if root:
            self.count(root, root.val, ctr, targetSum)
        return self.res