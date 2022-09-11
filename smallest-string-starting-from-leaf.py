class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ch = lambda i: chr(ord("a") + i)
        pos = {}
        def inorder(root, i):
            if root:
                inorder(root.left, 2 * i)
                pos[i] = root.val
                inorder(root.right, 2 * i + 1)
        inorder(root, 1)
        def getmin(i, j):
            oi, oj = i, j
            while i and j:
                if pos[i] < pos[j]:
                    return oi
                elif pos[i] > pos[j]:
                    return oj
                i = i // 2
                j = j // 2
            return oj or oi
        res = 0
        for i in pos:
            if 2 * i not in pos and 2 * i + 1 not in pos:
                res = getmin(res, i)
        smallest = []
        while res:
            smallest.append(ch(pos[res]))
            res = res // 2
        return "".join(smallest)