class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equalGraph = {}
        inequalities = []
        for eq in equations:
            a = eq[0]
            b = eq[-1]
            opr = eq[1:-1]
            if opr == "==":
                equalGraph[a] = equalGraph.get(a, []) + [b]
                equalGraph[b] = equalGraph.get(b, []) + [a]
            else:
                inequalities.append((a, b))
        for a, b in inequalities:
            paths = [a]
            visited = {a}
            while len(paths) > 0:
                curr = paths.pop()
                for j in equalGraph.get(curr, []):
                    if j not in visited:
                        visited.add(j)
                        paths.append(j)
            if b in visited:
                return False
        return True