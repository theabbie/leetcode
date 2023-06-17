class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        used = [False] * n
        i = 0
        s = k
        while True:
            if used[i]:
                break
            used[i] = True
            i = (i + s) % n
            s += k
        return [i + 1 for i in range(n) if not used[i]]