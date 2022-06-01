class Solution:
    def getSeq(self, num, i, n, a, b, ctr):
        if i >= n:
            return ctr >= 3
        for j in range(i + 1, n + 1):
            curr = int(num[i:j])
            if a == None or b == None or curr == a + b:
                if self.getSeq(num, j, n, b, curr, ctr + 1):
                    return True
            if num[i] == "0":
                break
        return False
    
    def isAdditiveNumber(self, num: str) -> bool:
        return self.getSeq(num, 0, len(num), None, None, 0)