# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if p or q:
                return False
            return True
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nodes = [(original, cloned)]
        while len(nodes) > 0:
            og, cl = nodes.pop()
            if self.isSameTree(og, target):
                return cl
            if og and cl:
                nodes.append((og.left, cl.left))
                nodes.append((og.right, cl.right))
        return None