class Solution:
    def diameter(self, root: 'Node') -> int:
        res = 0
        def d(r):
            nonlocal res
            a = b = 0
            mx = 0
            for x in r.children:
                h = d(x)
                mx = max(mx, h)
                t, a, b = sorted([h, a, b])
            res = max(res, a + b)
            return mx + 1
        d(root)
        return res