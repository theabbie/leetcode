class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        def nxt(c):
            c = ord(c) - ord('a')
            c += 1
            c %= 26
            return chr(ord('a') + c)
        def get(k, i):
            if i == 0:
                return "a"
            elif k <= pow(2, i - 1):
                return get(k, i - 1)
            elif operations[i - 1] == 0:
                return get(k - pow(2, i - 1), i - 1)
            return nxt(get(k - pow(2, i - 1), i - 1))
        return get(k, n)