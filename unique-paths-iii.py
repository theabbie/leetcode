class Solution:
    def getNeighbors(self, start, m, n):
        a, b = start
        neighbors = []
        if a > 0:
            neighbors.append((a - 1, b))
        if a < m - 1:
            neighbors.append((a + 1, b))
        if b > 0:
            neighbors.append((a, b - 1))
        if b < n - 1:
            neighbors.append((a, b + 1))
        return neighbors
    
    def unipaths(self, start, grid, visited, m, n, numEmpty):
        currval = grid[start[0]][start[1]]
        ways = 0
        if currval == -1:
            return ways
        if currval == 2:
            if len(visited) == numEmpty + 2:
                return ways + 1
            return ways
        neighbors = self.getNeighbors(start, m, n)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] != -1 and neighbor not in visited:
                ways += self.unipaths(neighbor, grid, visited.union({neighbor}), m, n, numEmpty)
        return ways
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numEmpty = 0
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    numEmpty += 1
                elif grid[i][j] == 1:
                    start = (i, j)
        return self.unipaths(start, grid, {start}, m, n, numEmpty)