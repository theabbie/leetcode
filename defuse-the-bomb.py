class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        p = [0]
        for i in range(3 * n):
            p.append(p[-1] + code[i % n])
        return [abs(p[n + i + int(k >= 0)]-p[n + i + k + int(k>=0)]) for i in range(n)]