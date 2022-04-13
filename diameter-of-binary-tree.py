# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return -1
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = float('-inf')
        nodes = [root]
        i = 0
        while i < len(nodes):
            curr = nodes[i]
            md = max(md, 2 + self.maxDepth(curr.left) + self.maxDepth(curr.right))
            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)
            i += 1
        return md