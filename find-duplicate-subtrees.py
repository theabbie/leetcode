# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def postorder(self, root, trees):
        s = "#"
        if root:
            s = f"{root.val},{self.postorder(root.left, trees)},{self.postorder(root.right, trees)}"
            trees[s].append(root)
        return s
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict(list)
        self.postorder(root, trees)
        return [trees[s][0] for s in trees if len(trees[s]) > 1]