# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeTree(self, nums, a, b):
        if a >= b:
            return None
        root = TreeNode()
        peak = max(range(a, b), key = lambda i: nums[i])
        root.val = nums[peak]
        root.left = self.makeTree(nums, a, peak)
        root.right = self.makeTree(nums, peak + 1, b)
        return root
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums, 0, len(nums))