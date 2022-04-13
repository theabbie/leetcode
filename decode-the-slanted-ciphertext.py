class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        m, n = rows, len(encodedText) // rows
        op = ""
        for i in range(n):
            for j in range(m):
                if i + j < n:
                    op += encodedText[(n + 1) * j + i]
        return op.rstrip()