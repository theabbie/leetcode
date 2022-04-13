class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            nn = 0
            while n != 0:
                c = n % 10
                nn += c * c
                n = n // 10
            n = nn
        return True