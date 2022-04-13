class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        encoded = []
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and dominoes[i] == dominoes[i + 1]:
                i += 1
                ctr += 1
            i += 1
            encoded.append([dominoes[i - 1], ctr])
        k = len(encoded)
        for i in range(k):
            c, ctr = encoded[i]
            left = encoded[i - 1][0] if i > 0 else "L"
            right = encoded[i + 1][0] if i < k - 1 else "R"
            if c == ".":
                if left == right:
                    encoded[i][0] = left
                if left == "R" and right == "L":
                    l = r = ctr >> 1
                    mid = ctr & 1
                    encoded[i][0] = "R" * l + "." * mid + "L" * r
                    encoded[i][1] = 1
        return "".join(c * ctr for c, ctr in encoded)