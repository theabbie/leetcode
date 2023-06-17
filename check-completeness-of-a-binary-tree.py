class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nodes = [(root, 0)]
        keys = {}
        while len(nodes) > 0:
            curr, l = nodes.pop()
            keys[l] = curr.val
            if curr.left:
                nodes.append((curr.left, 2 * l + 1))
            if curr.right:
                nodes.append((curr.right, 2 * l + 2))
        mkey = max(keys.keys())
        for l in range(mkey):
            if l not in keys:
                return False
        return True