import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.cx = x_center
        self.cy = y_center

    def randPoint(self) -> List[float]:
        randRadius = self.r * math.sqrt(random.random())
        randAngle = 2 * math.pi * random.random()
        x = self.cx + randRadius * math.cos(randAngle)
        y = self.cy + randRadius * math.sin(randAngle)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()