class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = 0
        curr = 0
        for c in moves:
            if c == "R" or c == "_":
                curr += 1
            else:
                curr -= 1
        res = max(res, abs(curr))
        curr = 0
        for c in moves:
            if c == "L" or c == "_":
                curr -= 1
            else:
                curr += 1
        res = max(res, abs(curr))
        return res