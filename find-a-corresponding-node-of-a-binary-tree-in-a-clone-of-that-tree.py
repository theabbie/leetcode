# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nodes = [(original, cloned)]
        while len(nodes) > 0:
            og, cp = nodes.pop()
            if og and cp:
                if og == target:
                    return cp
                nodes.append((og.left, cp.left))
                nodes.append((og.right, cp.right))
                