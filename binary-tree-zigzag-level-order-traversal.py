from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        levels = {}
        level = 0
        while len(queue) > 0:
            curr, level = queue.pop()
            if curr:
                levels[level] = levels.get(level, []) + [curr.val]
                queue.appendleft((curr.left, level + 1))
                queue.appendleft((curr.right, level + 1))
        return [levels[l][::1 - 2 * (l % 2)] for l in range(level)]