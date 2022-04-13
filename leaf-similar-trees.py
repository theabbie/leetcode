# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSeq(self, root):
        seq = []
        nodes = [root]
        while len(nodes) > 0:
            curr = nodes.pop()
            if curr:
                if not curr.left and not curr.right:
                    seq.append(curr.val)
                nodes.append(curr.left)
                nodes.append(curr.right)
        return seq
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafSeq(root1) == self.leafSeq(root2)