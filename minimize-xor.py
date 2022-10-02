class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = list("{:b}".format(num1))
        b2 = "{:b}".format(num2)
        ctr = b2.count("1")
        n = max(len(b1), len(b2))
        b1 = ["0"] * (n - len(b1)) + b1
        used = set()
        for b in range(n):
            if b1[b] == "1" and ctr > 0:
                b1[b] = "0"
                used.add(b)
                ctr -= 1
        for b in range(n - 1, -1, -1):
            if b not in used and ctr > 0:
                b1[b] = "1"
                ctr -= 1
        return num1 ^ int("".join(b1), 2)