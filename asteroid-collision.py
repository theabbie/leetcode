class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        survivors = set()
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(i)
            else:
                while len(stack) > 0 and abs(asteroids[stack[-1]]) < abs(asteroids[i]):
                    stack.pop()
                if len(stack) > 0:
                    if abs(asteroids[stack[-1]]) <= abs(asteroids[i]):
                        stack.pop()
                else:
                    survivors.add(i)
        for i in stack:
            survivors.add(i)
        return [asteroids[i] for i in range(n) if i in survivors]