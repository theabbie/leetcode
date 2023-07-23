from collections import deque

M = 998244353

q = int(input())

val = 1
digits = deque([1])
tinv = pow(10, M - 2, M)
pw = 1

for _ in range(q):
    curr = list(map(int, input().split()))
    if curr[0] == 1:
        val = 10 * val + curr[1]
        digits.append(curr[1])
        pw *= 10
        pw %= M
        val %= M
    if curr[0] == 2:
        x = len(digits)
        val = M + val - digits.popleft() * pw
        val %= M
        pw *= tinv
        pw %= M
    if curr[0] == 3:
        print(val)