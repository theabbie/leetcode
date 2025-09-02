class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        for start in range(2):
            prev = start
            for i in range(n):
                prev = derived[i] ^ prev
            if prev == start:
                return True
        return False