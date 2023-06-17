from collections import deque, defaultdict

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = defaultdict(int)
        sumparents = defaultdict(lambda: defaultdict(int))
        q = deque([(root, 0)])
        while len(q) > 0:
            curr, d = q.pop()
            if curr:
                sums[d] += curr.val
                q.appendleft((curr.left, d + 1))
                q.appendleft((curr.right, d + 1))
        q = deque([(root, root.val if root else 0, 0, 0)])
        while len(q) > 0:
            curr, currval, other, d = q.pop()
            curr.val = sums[d] - currval - other
            if curr.left:
                q.appendleft((curr.left, curr.left.val, curr.right.val if curr.right else 0, d + 1))
            if curr.right:
                q.appendleft((curr.right, curr.right.val, curr.left.val if curr.left else 0, d + 1))
        return root