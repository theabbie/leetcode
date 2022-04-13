# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.exists = set()
        nodes = [(self.root, 0)]
        while len(nodes) > 0:
            curr, l = nodes.pop()
            if curr:
                self.exists.add(l)
                nodes.append((curr.left, 2 * l + 1))
                nodes.append((curr.right, 2 * l + 2))

    def find(self, target: int) -> bool:
        return target in self.exists

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)