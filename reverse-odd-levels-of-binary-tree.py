from collections import deque, defaultdict

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, 0)])
        levels = defaultdict(list)
        while len(q) > 0:
            curr, l = q.pop()
            if curr:
                levels[l].append(curr.val)
                q.appendleft((curr.left, l + 1))
                q.appendleft((curr.right, l + 1))
        q = deque([(root, 0)])
        while len(q) > 0:
            curr, l = q.pop()
            if curr:
                if l % 2 == 1:
                    curr.val = levels[l].pop()
                q.appendleft((curr.left, l + 1))
                q.appendleft((curr.right, l + 1))
        return root