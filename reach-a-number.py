class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        total = 0
        steps = 0
        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps
        return steps