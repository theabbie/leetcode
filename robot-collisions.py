class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        vals = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        vals.sort()
        stack = []
        for p, h, d, pos in vals:
            if d == "L":
                add = True
                while stack and stack[-1][2] == "R":
                    if stack[-1][1] < h:
                        stack.pop()
                        h -= 1
                    elif stack[-1][1] > h:
                        stack[-1][1] -= 1
                        add = False
                        break
                    else:
                        stack.pop()
                        add = False
                        break
                if add:
                    stack.append([p, h, d, pos])
            else:
                stack.append([p, h, d, pos])
        stack.sort(key = lambda x: x[3])
        return [x[1] for x in stack]