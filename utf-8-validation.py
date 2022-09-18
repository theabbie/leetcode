class Solution:
    def getbin(self, num):
        return "{:08b}".format(num)
    
    def getctr(self, num):
        b = self.getbin(num)
        i = 0
        while i < 8 and b[i] == "1":
            i += 1
        return i
    
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            ctr = self.getctr(data[i])
            if ctr > 4 or ctr == 1:
                return False
            if i + ctr > n:
                return False
            j = i + ctr
            i += 1
            while i < j:
                if self.getctr(data[i]) != 1:
                    return False
                i += 1
        return True