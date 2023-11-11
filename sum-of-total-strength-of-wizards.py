class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(strength)
        stack = []
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        for i in range(n):
            while len(stack) > 0 and strength[i] < strength[stack[-1]]:
                curr = stack.pop()
                next_smaller[curr] = i
            if len(stack) > 0:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + strength[i]
        pp = [0] * (n + 2)
        for i in range(n + 1):
            pp[i + 1] += pp[i] + p[i]
        res = 0
        for i in range(n):
            l = prev_smaller[i]
            r = next_smaller[i]
            res += strength[i] * (i - l) * (pp[r + 1] - pp[i + 1])
            res %= M
            res -= strength[i] * (r - i) * (pp[i + 1] - pp[l + 1])
            res %= M
        res = (M + res) % M
        return res