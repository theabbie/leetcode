# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isInTree(self, root, node):
#         if root:
#             if root.val == node.val:
#                 return True
#             if self.isInTree(root.left, node) or self.isInTree(root.right, node):
#                 return True
#         return False
    
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root:
#             if root.val == p.val or root.val == q.val:
#                 return root
#             pInLeft = self.isInTree(root.left, p)
#             qInLeft = self.isInTree(root.left, q)
#             if pInLeft and qInLeft:
#                 return self.lowestCommonAncestor(root.left, p, q)
#             if not pInLeft and not qInLeft:
#                 return self.lowestCommonAncestor(root.right, p, q)
#             if pInLeft ^ qInLeft:
#                 return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodepaths = [None, None]
        paths = [[root]]
        while len(paths) > 0:
            curr = paths.pop()
            if curr[-1].val == p.val:
                nodepaths[0] = curr
            if curr[-1].val == q.val:
                nodepaths[1] = curr
            if nodepaths[0] and nodepaths[1]:
                break
            if curr[-1].left:
                paths.append(curr + [curr[-1].left])
            if curr[-1].right:
                paths.append(curr + [curr[-1].right])
        i = 0
        k = min(len(nodepaths[0]), len(nodepaths[1]))
        while nodepaths[0][i].val == nodepaths[1][i].val:
            i += 1
            if i >= k:
                break
        return nodepaths[0][i - 1]