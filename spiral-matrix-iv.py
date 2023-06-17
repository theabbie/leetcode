class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        k = 2 * min(m, n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, -1
        for d in range(k):
            if not head:
                break
            for i in range(n):
                x += dx[d % 4]
                y += dy[d % 4]
                res[x][y] = head.val
                head = head.next
                if not head:
                    break
            m, n = n, m - 1
        return res
        