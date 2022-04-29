class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set([tuple(c) for c in obstacles])
        x, y = 0, 0
        direction = 0
        mdist = 0
        for c in commands:
            if c == -2:
                direction = (direction + 3) % 4
            elif c == -1:
                direction = (direction + 1) % 4
            else:
                if direction == 0:
                    for i in range(c):
                        if (x, y + 1) not in obstacles:
                            y += 1
                elif direction == 1:
                    for i in range(c):
                        if (x + 1, y) not in obstacles:
                            x += 1
                elif direction == 2:
                    for i in range(c):
                        if (x, y - 1) not in obstacles:
                            y -= 1
                elif direction == 3:
                    for i in range(c):
                        if (x - 1, y) not in obstacles:
                            x -= 1
                mdist = max(mdist, x * x + y * y)
        return mdist