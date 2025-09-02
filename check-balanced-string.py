class Solution:
    def isBalanced(self, num: str) -> bool:
        s = [0, 0]
        for i in range(len(num)):
            s[i % 2] += int(num[i])
        return s[0] == s[1]