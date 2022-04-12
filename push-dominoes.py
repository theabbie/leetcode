class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dominoes = list(dominoes)
        encoded = []
        op = ""
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and dominoes[i] == dominoes[i + 1]:
                i += 1
                ctr += 1
            i += 1
            encoded.append((dominoes[i - 1], ctr))
        k = len(encoded)
        for i in range(k):
            c, ctr = encoded[i]
            if c == ".":
                if i == 0:
                    if i < k - 1 and encoded[i + 1][0] == "L":
                        op += "L" * ctr
                    else:
                        op += "." * ctr
                elif i == k - 1:
                    if i > 0 and encoded[i - 1][0] == "R":
                        op += "R" * ctr
                    else:
                        op += "." * ctr
                else:
                    if encoded[i - 1][0] == "L" and encoded[i + 1][0] == "R":
                        op += "." * ctr
                    if encoded[i - 1][0] == "L" and encoded[i + 1][0] == "L":
                        op += "L" * ctr
                    if encoded[i - 1][0] == "R" and encoded[i + 1][0] == "R":
                        op += "R" * ctr
                    if encoded[i - 1][0] == "R" and encoded[i + 1][0] == "L":
                        l = ctr // 2
                        mid = ctr - 2 * (ctr // 2)
                        r = ctr // 2
                        op += "R" * l + "." * mid + "L" * r
            else:
                op += c * ctr
        return op