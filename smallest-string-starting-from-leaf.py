# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = [(root, [root.val] if root else [])]
        i = 0
        smallest = None
        while i < len(paths):
            curr, val = paths[i]
            if curr:
                if not curr.left and not curr.right:
                    n = len(val)
                    currval = "".join(["abcdefghijklmnopqrstuvwxyz"[val[i]] for i in range(n - 1, -1, -1)])
                    if smallest:
                        if currval < smallest:
                            smallest = currval
                    else:
                        smallest = currval
                if curr.left:
                    paths.append((curr.left, val + [curr.left.val]))
                if curr.right:
                    paths.append((curr.right, val + [curr.right.val]))
            i += 1
        return smallest