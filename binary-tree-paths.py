# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        op = []
        paths = [[root]]
        while len(paths) > 0:
            curr = paths.pop()
            if curr[-1].left or curr[-1].right:
                if curr[-1].left:
                    paths.append(curr + [curr[-1].left])
                if curr[-1].right:
                    paths.append(curr + [curr[-1].right])
            else:
                op.append(curr)
        return ["->".join([str(node.val) for node in path]) for path in op]