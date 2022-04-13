# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        mroot = TreeNode()
        nodes = [(mroot, root1, root2)]
        while len(nodes) > 0:
            mcurr, curr1, curr2 = nodes.pop()
            if mcurr:
                mcurr.val = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0)
            if curr1 or curr2:
                mcurr.left = TreeNode() if (curr1 and curr1.left) or (curr2 and curr2.left) else None
                mcurr.right = TreeNode() if (curr1 and curr1.right) or (curr2 and curr2.right) else None
                nodes.append((mcurr.left, curr1.left if curr1 else None, curr2.left if curr2 else None))
                nodes.append((mcurr.right, curr1.right if curr1 else None, curr2.right if curr2 else None))
        return mroot