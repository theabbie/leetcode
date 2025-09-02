class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        def gen(i, curr):
            if i >= n:
                return len(curr) >= 3
            v = 0
            for j in range(i, n):
                v = 10 * v + int(num[j])
                if v.bit_length() >= 32:
                    break
                if len(curr) < 2 or v == curr[-2] + curr[-1]:
                    curr.append(v)
                    if gen(j + 1, curr):
                        return True
                    curr.pop()
                if len(curr) >= 2 and v > curr[-2] + curr[-1]:
                    break
                if num[i] == '0':
                    break
            return False
        res = []
        gen(0, res)
        return res