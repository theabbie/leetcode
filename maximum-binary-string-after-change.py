class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        i = 0
        while i < n and binary[i] == "1":
            i += 1
        o = z = 0
        for j in range(i, n):
            if binary[j] == "0":
                z += 1
            else:
                o += 1
        return "1" * i + "1" * max(z - 1, 0) + "0" * min(z, 1) + "1" * o