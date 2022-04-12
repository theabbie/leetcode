class Solution:
    def isValid(self, x, y):
        if x < 0 or y < 0 or x >= 8 or y >= 8:
            return False
        return True
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        x, y = king
        queens = set([tuple(q) for q in queens])
        op = []
        for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            n = 1
            while self.isValid(x + n * dx, y + n * dy):
                if (x + n * dx, y + n * dy) in queens:
                    op.append([x + n * dx, y + n * dy])
                    break
                n += 1
        return op