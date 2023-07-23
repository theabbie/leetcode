class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        vals = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        vals.sort()
        stack = []
        for p, h, d, pos in vals:
            if d == "R":
                stack.append((p, h, d, pos))
                continue
            gone = False
            while len(stack) > 0 and stack[-1][1] <= h and stack[-1][2] == "R":
                if stack[-1][1] == h:
                    stack.pop()
                    gone = True
                    break
                h -= 1
                stack.pop()
            if not gone and len(stack) > 0 and stack[-1][2] == "R" and stack[-1][1] > h:
                stack[-1] = (stack[-1][0], stack[-1][1] - 1, stack[-1][2], stack[-1][3])
                gone = True
            if not gone:
                stack.append((p, h, d, pos))
        return [s[1] for s in sorted(stack, key = lambda x: x[3])]