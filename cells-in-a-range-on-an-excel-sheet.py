class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        beg, end = s.split(":")
        a = ord(beg[0])
        m = int(beg[1])
        b = ord(end[0])
        n = int(end[1])
        return [chr(x) + str(y) for x in range(a, b + 1) for y in range(m, n + 1)]