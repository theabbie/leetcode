class Solution:
    def getSteps(self, curr):
        steps = set()
        for i in range(4):
            for d in [1, -1]:
                now = list(curr)
                now[i] = (10 + now[i] + d) % 10
                steps.add(tuple(now))
        return steps
    
    def openLock(self, deadends: List[str], target: str) -> int:
        beg = (0, 0, 0, 0)
        target = tuple(int(d) for d in target)
        paths = [(beg, 0)]
        visited = {beg}
        for end in deadends:
            end = tuple(int(d) for d in end)
            if beg == end:
                return -1
            visited.add(end)
        i = 0
        while i < len(paths):
            curr, steps = paths[i]
            if curr == target:
                return steps
            for j in self.getSteps(curr):
                if j not in visited:
                    visited.add(j)
                    paths.append((j, steps + 1))
            i += 1
        return -1