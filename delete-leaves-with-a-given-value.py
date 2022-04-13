# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right
    
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        while True:
            if not root:
                break
            if self.isLeaf(root) and root.val == target:
                return None
            numDeleted = 0
            nodes = [root]
            i = 0
            while i < len(nodes):
                curr = nodes[i]
                if curr.left:
                    if self.isLeaf(curr.left) and curr.left.val == target:
                        curr.left = None
                        numDeleted += 1
                    else:
                        nodes.append(curr.left)
                if curr.right:
                    if self.isLeaf(curr.right) and curr.right.val == target:
                        curr.right = None
                        numDeleted += 1
                    else:
                        nodes.append(curr.right)
                i += 1
            if numDeleted == 0:
                break
        return root