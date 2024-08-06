def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def mid(a, b):
    x = a[0] * b[1] + a[1] * b[0]
    y = 2 * a[1] * b[1]
    mul = gcd(x, y)
    x //= mul
    y //= mul
    return (x, y)

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        res = []
        M = 0
        def dfs(rt, l, r, d):
            if not rt:
                return
            nonlocal res, M
            m = mid(l, r)
            M = max(M, m[1])
            if d + 1 > len(res):
                res.append([])
            res[d].append((m, rt.val))
            dfs(rt.left, l, m, d + 1)
            dfs(rt.right, m, r, d + 1)
        dfs(root, (0, 1), (1, 1), 0)
        def get(arr):
            val = [""] * (M - 1)
            for pos, v in arr:
                val[pos[0] * M // pos[1] - 1] = str(v)
            return val
        return [get(el) for el in res]