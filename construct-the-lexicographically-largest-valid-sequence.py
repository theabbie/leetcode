class Solution:
    def constructDistancedSequence(self, n):
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def construct(i):
            if i == len(res):
                return True
            if res[i]:
                return construct(i + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                used[num] = True
                res[i] = num
                valid = False
                if num == 1:
                    valid = construct(i + 1)
                elif i + num < len(res) and res[i + num] == 0:
                    res[i + num] = num
                    valid = construct(i + 1)
                    if not valid:
                        res[i + num] = 0
                if valid:
                    return True
                res[i] = 0
                used[num] = False
            return False

        construct(0)
        return res