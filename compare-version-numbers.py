class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = [int(r) for r in version1.split(".")]
        b = [int(r) for r in version2.split(".")]
        if len(a) < len(b):
            a += [0] * (len(b) - len(a))
        else:
            b += [0] * (len(a) - len(b))
        if tuple(a) > tuple(b):
            return 1
        elif tuple(a) < tuple(b):
            return -1
        return 0