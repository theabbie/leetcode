from collections import defaultdict

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        stack = [self.king]
        while len(stack) > 0:
            curr = stack.pop()
            if curr not in self.dead:
                res.append(curr)
            for j in self.graph[curr][::-1]:
                stack.append(j)
        return res