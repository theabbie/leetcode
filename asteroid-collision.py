class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while True:
            n = len(asteroids)
            stack = []
            op = []
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
                        op.append(i)
            op = sorted(stack + op)
            op =  [asteroids[i] for i in op]
            if asteroids == op:
                return op
            else:
                asteroids = op