class Node:
    def __init__(self, val = None, ctr = 1, left = None, right = None):
        self.val = val
        self.ctr = ctr
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, root):
        if not node:
            return root
        if not root:
            return node
        if node.val < root.val:
            root.left = self._insert(node, root.left)
        elif node.val > root.val:
            root.right = self._insert(node, root.right)
        else:
            root.ctr += 1
        return root

    def insert(self, val):
        self.root = self._insert(Node(val), self.root)

    def _delete(self, val, root):
        if not root:
            return None
        if root.val == val:
            if root.ctr > 1:
                root.ctr -= 1
                return root
            else:
                root = self._insert(root.right, root.left)
                return root
        if val <= root.val:
            root.left = self._delete(val, root.left)
        else:
            root.right = self._delete(val, root.right)
        return root

    def delete(self, val):
        self.root = self._delete(val, self.root)

    def _inorder(self, root, res):
        if root:
            self._inorder(root.left, res)
            res.extend([root.val] * root.ctr)
            self._inorder(root.right, res)

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

arr = [5, 2, 7, 7, 9, 9, 1, 9, 6, 10, 6, 4, 8, 3]

bst = BST()

for el in arr:
    bst.insert(el)

print(bst.inorder())

for el in arr[-5:]:
    bst.delete(el)

print(bst.inorder())