class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        nodes = []
        def DFS(r):
            if r:
                nodes.append(r)
                DFS(r.left)
                DFS(r.right)
        DFS(root)
        def DFS(r, v):
            v.add(r.val)
            if r.left:
                if r.left.val not in to_delete:
                    DFS(r.left, v)
                else:
                    r.left = None
            if r.right:
                if r.right.val not in to_delete:
                    DFS(r.right, v)
                else:
                    r.right = None
        res = set()
        v = set()
        for r in nodes:
            if r.val not in v and r.val not in to_delete:
                res.add(r)
                v.add(r.val)
                DFS(r, v)
        return res