class Solution:
    def minMoves(self, classroom, energy):
        n = len(classroom)
        m = len(classroom[0])
        lmap = {}
        lc = 0
        for i in range(n):
            for j in range(m):
                if classroom[i][j] == 'L':
                    lmap[(i, j)] = lc
                    lc += 1
                elif classroom[i][j] == 'S':
                    sr = i
                    sc = j
        fullmask = (1 << lc) - 1
        best = [[[-1] * (1 << lc) for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((sr, sc, energy, 0, 0))
        best[sr][sc][0] = energy

        while q:
            r, c, e, mask, steps = q.popleft()

            if mask == fullmask:
                return steps

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                cell = classroom[nr][nc]
                if cell == 'X':
                    continue

                ne = e - 1
                if ne < 0:
                    continue

                if cell == 'R':
                    ne = energy

                nmask = mask
                if cell == 'L':
                    nmask |= 1 << lmap[(nr, nc)]

                if ne <= best[nr][nc][nmask]:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, ne, nmask, steps + 1))

        return -1