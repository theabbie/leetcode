class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        mvals = {}
        nodes = [(root, 0)]
        mlevel = -1
        while len(nodes) > 0:
            curr, l = nodes.pop()
            if curr:
                mlevel = max(mlevel, l)
                mvals[l] = max(mvals.get(l, float('-inf')), curr.val)
                nodes.append((curr.left, l + 1))
                nodes.append((curr.right, l + 1))
        return [mvals[l] for l in range(mlevel + 1)]