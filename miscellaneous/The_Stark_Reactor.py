k = int(input())

decays = []

def countSol(coeff, n, rhs):
    print(coeff, rhs)
    dp = [0 for _ in range(rhs + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(coeff[i], rhs + 1):
            dp[j] += dp[j - coeff[i]]
    return dp[rhs]

for _ in range(k):
    a, b = map(int, input().split())
    decays.append((a, b))

q = int(input())

for _ in range(q):
    m1, z1, m2, z2 = map(int, input().split())
    x = m1 - m2
    y = z1 - z2
    print(countSol([a for a, b in decays], k, x))
    print(countSol([b for a, b in decays], k, y))