# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = {}
        paths = [(root, 0)]
        while len(paths) > 0:
            curr, i = paths.pop()
            if curr:
                tree[i] = curr.val
                paths.append((curr.left, 2 * i + 1))
                paths.append((curr.right, 2 * i + 2))
        return ";".join(["{}={}".format(k, v) for k, v in tree.items()])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(";")
        tree = {}
        for v in vals:
            if len(v) > 0:
                key, value = v.split("=")
                tree[int(key)] = int(value)
        if len(tree) == 0:
            return None
        root = TreeNode()
        paths = [(root, 0)]
        while len(paths) > 0:
            curr, i = paths.pop()
            curr.val = tree[i]
            if (2 * i + 1) in tree:
                curr.left = TreeNode()
                paths.append((curr.left, 2 * i + 1))
            if (2 * i + 2) in tree:
                curr.right = TreeNode()
                paths.append((curr.right, 2 * i + 2))
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))