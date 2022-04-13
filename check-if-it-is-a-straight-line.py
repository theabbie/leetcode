class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        m = None
        for i in range(1, n):
            dy = coordinates[i][1] - coordinates[0][1]
            dx = coordinates[i][0] - coordinates[0][0]
            sign = -1 if (dx >= 0) ^ (dy >= 0) else 1
            if dx == 0 or dy == 0:
                sign = 1
            curr = (sign, abs(dy), abs(dx))
            mul = self.gcd(curr[1], curr[2])
            if mul > 0:
                curr = (curr[0], curr[1] // mul, curr[2] // mul)
            if m:
                if curr != m:
                    return False
            else:
                m = curr
        return True
