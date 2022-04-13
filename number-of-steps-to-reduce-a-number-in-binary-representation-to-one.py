class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1":
            if s[-1] == "0":
                s = s[:-1]
            else:
                i = len(s) - 1
                carry = 1
                while carry > 0 and i >= 0:
                    curr = int(s[i]) + carry
                    s = s[:i] + str(curr % 2) + s[i+1:]
                    carry = curr // 2
                    i -= 1
                if carry > 0:
                    s = "1" + s
            steps += 1
        return steps