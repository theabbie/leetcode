# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mlen(self, root):
        if not root:
            return 0
        l = self.mlen(root.left)
        r = self.mlen(root.right)
        mpath = 1
        if root.left and root.left.val == root.val:
            mpath = max(mpath, 1 + l)
            self.pathlen = max(self.pathlen, 1 + l)
        if root.right and root.right.val == root.val:
            mpath = max(mpath,  1 + r)
            self.pathlen = max(self.pathlen, 1 + r)
        if root.left and root.right and root.val == root.left.val == root.right.val:
            self.pathlen = max(self.pathlen, l + r + 1)
        return mpath
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.pathlen = 0
        self.mlen(root)
        return max(self.pathlen - 1, 0)