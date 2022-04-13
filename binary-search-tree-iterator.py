# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.inorder(root)
        self.i = -1
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.list.append(root.val)
            self.inorder(root.right)

    def next(self) -> int:
        self.i += 1
        return self.list[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.list) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()