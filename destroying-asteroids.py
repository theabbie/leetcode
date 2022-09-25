class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(key = lambda el: (el, el) if el <= mass else (float('inf'), el))
        for s in asteroids:
            if mass >= s:
                mass += s
            else:
                return False
        return True