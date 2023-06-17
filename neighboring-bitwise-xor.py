class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        for first in range(2):
            newarr = [first] * n
            for i in range(n):
                newarr[(i + 1) % n] = newarr[i] ^ derived[i]
            if newarr[0] == first:
                return True
        return False