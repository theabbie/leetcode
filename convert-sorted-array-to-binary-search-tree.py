# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n > 1:
            root = TreeNode(nums[n // 2])
            root.left = self.sortedArrayToBST(nums[:n//2])
            root.right = self.sortedArrayToBST(nums[1 + (n//2) :])
            return root
        elif n == 1:
            return TreeNode(val = nums[0])
        else:
            return None