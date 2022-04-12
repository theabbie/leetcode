class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry > 0 and i >= 0:
            val = digits[i] + carry
            digits[i] = val % 10
            carry = val // 10
            i -= 1
        if carry > 0:
            digits.insert(0, carry)
        return digits