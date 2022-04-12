class Solution:
    def isValidChunk(self, s):
        if len(s) > 1 and s[0] == "0":
            return False
        if int(s) < 0 or int(s) > 255:
            return False
        return True
    
    def getAddress(self, s, curr, i, n):
        op = []
        if len(curr) == 4 and i == n:
            return [curr]
        for j in range(i + 1, n + 1):
            chunk = s[i:j]
            if self.isValidChunk(chunk):
                val = self.getAddress(s, curr + [chunk], j, n)
                op.extend(val)
        return op
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        val = self.getAddress(s, [], 0, len(s))
        return [".".join(v) for v in val]