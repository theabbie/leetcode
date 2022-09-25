class Solution:
    def numCollide(self, directions):
        stack = []
        for s in directions:
            if s == "L":
                if len(stack) > 0 and stack[-1] != "L":
                    self.res += 1
                    if stack[-1] == "R":
                        self.res += 1
                    stack.pop()
                    stack.append("S")
                else:
                    stack.append(s)
            else:
                stack.append(s)
        return stack
    
    def countCollisions(self, directions: str) -> int:
        self.res = 0
        stack = self.numCollide(directions)
        directions = "".join(({ "L": "R", "R": "L", "S": "S" })[el] for el in stack[::-1])
        self.numCollide(directions)
        return self.res