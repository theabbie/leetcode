class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) == len(s) and goal in s + s:
            return True
        return False