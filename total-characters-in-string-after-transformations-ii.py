M = 10 ** 9 + 7

def mat_mult(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % M
    return result

def mat_pow(mat, exp):
    size = len(mat)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = mat
    while exp > 0:
        if exp % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        exp //= 2
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mul = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for c in range(i + 1, i + nums[i] + 1):
                mul[c % 26][i] += 1
        ctr = [0] * 26
        for c in s:
            ctr[ord(c) - ord('a')] += 1
        mul = mat_pow(mul, t)
        res = [0] * 26
        for i in range(26):
            for j in range(26):
                res[i] = (res[i] + mul[i][j] * ctr[j]) % M
        return sum(res) % M