from collections import deque, defaultdict

class Solution:
    def minSwap(self, arr):
        n = len(arr)
        res = 0
        oldarr = arr[:]
        h = {}
        oldarr.sort()
        for i in range(n):
            h[arr[i]] = i
        init = 0
        for i in range(n):
            if arr[i] != oldarr[i]:
                res += 1
                init = arr[i]
                arr[i], arr[h[oldarr[i]]] = arr[h[oldarr[i]]], arr[i]
                h[init] = h[oldarr[i]]
                h[oldarr[i]] = i
        return res
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        levels = defaultdict(list)
        while len(q) > 0:
            curr, l = q.pop()
            if curr:
                levels[l].append(curr.val)
                q.appendleft((curr.left, l + 1))
                q.appendleft((curr.right, l + 1))
        res = 0
        for l in levels:
            res += self.minSwap(levels[l])
        return res