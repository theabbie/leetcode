class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for s in asteroids:
            if s < 0:
                exists = True
                while len(stack) > 0 and stack[-1] > 0:
                    if abs(stack[-1]) > abs(s):
                        exists = False
                        break
                    elif abs(stack[-1]) == abs(s):
                        exists = False
                        stack.pop()
                        break
                    stack.pop()
                if exists:
                    stack.append(s)
            else:
                stack.append(s)
        return stack