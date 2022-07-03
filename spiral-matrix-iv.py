class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(m)]
        mark = -1
        ctr = 0
        direction = 0
        x, y = 0, 0
        prev = (-1, -1)
        curr = head
        while curr and ctr < m * n:
            if matrix[x][y] == mark and (x, y) != prev:
                matrix[x][y] = curr.val
                curr = curr.next
                prev = (x, y)
            switch = False
            if direction == 0:
                if (y + 1) < n and matrix[x][y + 1] == mark:
                    y += 1
                else:
                    switch = True
            elif direction == 1:
                if (x + 1) < m and matrix[x + 1][y] == mark:
                    x += 1
                else:
                    switch = True
            elif direction == 2:
                if (y - 1) >= 0 and matrix[x][y - 1] == mark:
                    y -= 1
                else:
                    switch = True
            else:
                if (x - 1) >= 0 and matrix[x - 1][y] == mark:
                    x -= 1
                else:
                    switch = True
            if switch:
                direction = (direction + 1) % 4
        return matrix