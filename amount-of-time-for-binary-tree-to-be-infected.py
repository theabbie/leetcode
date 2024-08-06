from collections import deque, defaultdict

class Solution:
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
            self.graph[root.val].add(root.left.val)
            self.graph[root.left.val].add(root.val)
        if root.right:
            self.inorder(root.right)
            self.graph[root.val].add(root.right.val)
            self.graph[root.right.val].add(root.val)
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        self.graph = defaultdict(set)
        self.inorder(root)
        q = deque([(start, 0)])
        v = {start}
        maxt = 0
        while len(q) > 0:
            curr, t = q.pop()
            maxt = t
            for j in self.graph[curr]:
                if j not in v:
                    v.add(j)
                    q.appendleft((j, t + 1))
        return maxt