class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = set()
        visited.add((x, y))
        for c in path:
            if c == 'N':
                y += 1
            if c == 'E':
                x += 1
            if c == 'S':
                y -= 1
            if c == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False