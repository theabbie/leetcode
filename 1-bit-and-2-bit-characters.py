class Solution:
    def isValid(self, bits, i):
        if i == 0:
            if bits[0] == 0:
                return True
            else:
                return False
        if i == 1:
            if bits[0] == 1:
                return True
            elif bits[1] == 0:
                return True
            else:
                return False
        if bits[i - 1] == 1 and self.isValid(bits, i - 2):
            return True
        if bits[i] == 0 and self.isValid(bits, i - 1):
            return True
        return False
    
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) >= 2:
            return self.isValid(bits, len(bits) - 2)
        else:
            return True