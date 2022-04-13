# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfTree(self, root):
        if root:
            curr = root.val + self.sumOfTree(root.left) + self.sumOfTree(root.right)
            self.sums[curr] = self.sums.get(curr, 0) + 1
            return curr
        return 0
    
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sums = {}
        self.sumOfTree(root)
        mfreq = max(self.sums.values())
        return [k for k, v in self.sums.items() if v == mfreq]