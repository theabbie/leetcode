class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(r):
            if not r:
                return []
            return dfs(r.left) + [r.val] + dfs(r.right)
        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            res.extend(a[i:])
            res.extend(b[j:])
            return res
        return merge(dfs(root1), dfs(root2))