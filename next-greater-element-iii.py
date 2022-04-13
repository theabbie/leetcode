class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        k = len(digits)
        i = k - 1
        while i > 0:
            if digits[i - 1] < digits[i]:
                break
            i -= 1
        if i == 0:
            return -1
        closest = i
        for j in range(i, k):
            if digits[j] > digits[i - 1] and digits[j] - digits[i - 1] <= digits[closest] - digits[i - 1]:
                closest = j
        digits[i - 1], digits[closest] = digits[closest], digits[i - 1]
        op = 0
        for d in range(i):
            op = 10 * op + digits[d]
        for d in range(k - 1, i - 1, -1):
            op = 10 * op + digits[d]
        return op if op <= ((1 << 31) - 1) else -1